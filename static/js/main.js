const PYODIDE_SCRIPT_URL = "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/pyodide.js";

let pyodideReadyPromise = null;
const trackedViews = new Set();

function getCookie(name) {
    const cookies = document.cookie ? document.cookie.split(";") : [];

    for (const cookie of cookies) {
        const trimmedCookie = cookie.trim();
        if (trimmedCookie.startsWith(`${name}=`)) {
            return decodeURIComponent(trimmedCookie.slice(name.length + 1));
        }
    }

    return "";
}

function getRecaptchaToken(action) {
    const siteKey = document.querySelector('meta[name="recaptcha-site-key"]')?.content;

    return new Promise((resolve) => {
        if (!siteKey || typeof grecaptcha === "undefined") {
            // Not configured yet — the server treats a missing token as
            // "unverified" only when reCAPTCHA is actually turned on.
            resolve(null);
            return;
        }

        try {
            grecaptcha.ready(() => {
                grecaptcha
                    .execute(siteKey, { action })
                    .then(resolve)
                    .catch(() => resolve(null));
            });
        } catch (error) {
            resolve(null);
        }
    });
}

async function trackEngagement(eventType, options = {}) {
    const endpoint = document.querySelector('meta[name="engagement-endpoint"]')?.content;
    if (!endpoint) {
        return;
    }

    const payload = JSON.stringify({
        event_type: eventType,
        page_path: window.location.pathname,
        lesson_slug: options.lessonSlug || null,
        metadata: options.metadata || {},
    });

    // Same-tab navigations (e.g. an outbound CTA click) can unload the page
    // before a fetch() finishes. sendBeacon is designed to survive that.
    if (options.beacon && navigator.sendBeacon) {
        navigator.sendBeacon(endpoint, new Blob([payload], { type: "application/json" }));
        return;
    }

    try {
        await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin",
            body: payload,
        });
    } catch (error) {
        // Tracking should never interrupt learning interactions.
        console.debug("Engagement tracking failed.", error);
    }
}

function loadExternalScript(src) {
    return new Promise((resolve, reject) => {
        const existing = document.querySelector(`script[src="${src}"]`);
        if (existing) {
            if (existing.dataset.loaded === "true") {
                resolve();
                return;
            }
            existing.addEventListener("load", () => resolve(), { once: true });
            existing.addEventListener("error", () => reject(new Error("Failed to load script.")), { once: true });
            return;
        }

        const script = document.createElement("script");
        script.src = src;
        script.async = true;
        script.addEventListener("load", () => {
            script.dataset.loaded = "true";
            resolve();
        }, { once: true });
        script.addEventListener("error", () => reject(new Error("Failed to load script.")), { once: true });
        document.head.appendChild(script);
    });
}

async function getPyodide() {
    if (!pyodideReadyPromise) {
        pyodideReadyPromise = (async () => {
            await loadExternalScript(PYODIDE_SCRIPT_URL);
            return window.loadPyodide({
                stdout: () => {},
                stderr: () => {},
            });
        })();
    }

    return pyodideReadyPromise;
}

async function runPython(panel) {
    const source = panel.querySelector("[data-python-source]");
    const output = panel.querySelector("[data-python-output]");
    const runButton = panel.querySelector("[data-run-python]");
    const stdinField = panel.querySelector("[data-python-stdin]");
    const lessonSlug = panel.dataset.lessonSlug || "";

    if (!source || !output || !runButton) {
        return;
    }

    const originalLabel = runButton.textContent;
    output.textContent = "Loading Python runtime...";
    runButton.disabled = true;
    runButton.textContent = "Running...";

    try {
        const pyodide = await getPyodide();

        const stdinLines = stdinField && stdinField.value
            ? stdinField.value.split("\n")
            : [];
        pyodide.setStdin({
            stdin: () => (stdinLines.length ? stdinLines.shift() : ""),
        });

        const result = await pyodide.runPythonAsync(`
import io
import sys
from contextlib import redirect_stdout, redirect_stderr

buffer = io.StringIO()

with redirect_stdout(buffer), redirect_stderr(buffer):
    exec(${JSON.stringify(source.value)})

buffer.getvalue()
        `);

        output.textContent = result || "Code ran successfully with no output.";
        output.dataset.status = "success";
        trackEngagement("code_run", {
            lessonSlug,
            metadata: {
                status: "success",
                source_length: source.value.length,
                output_length: output.textContent.length,
            },
        });
    } catch (error) {
        output.textContent = error.message || "Something went wrong while running the code.";
        output.dataset.status = "error";
        trackEngagement("code_run", {
            lessonSlug,
            metadata: {
                status: "error",
                source_length: source.value.length,
                error_message: output.textContent.slice(0, 255),
            },
        });
    } finally {
        runButton.disabled = false;
        runButton.textContent = originalLabel;
    }
}

async function requestAiHint(panel) {
    const hintButton = panel.querySelector("[data-ai-hint]");
    const hintOutput = panel.querySelector("[data-ai-hint-output]");
    const source = panel.querySelector("[data-python-source]");
    const output = panel.querySelector("[data-python-output]");

    if (!hintButton || !hintOutput || !source) {
        return;
    }

    const endpoint = hintButton.dataset.hintUrl;
    if (!endpoint) {
        return;
    }

    const originalLabel = hintButton.textContent;
    hintButton.disabled = true;
    hintButton.textContent = "Thinking...";
    hintOutput.hidden = false;
    hintOutput.textContent = "Getting a hint...";

    try {
        const recaptchaToken = await getRecaptchaToken("ai_code_hint");
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            credentials: "same-origin",
            body: JSON.stringify({
                title: panel.dataset.hintTitle || "",
                goal: panel.dataset.hintGoal || "",
                code: source.value,
                output: output ? output.textContent : "",
                is_error: output ? output.dataset.status === "error" : false,
                recaptcha_token: recaptchaToken,
            }),
        });
        const data = await response.json();
        hintOutput.textContent = data.ok ? data.hint : (data.error || "Hint isn't available right now.");
    } catch (error) {
        hintOutput.textContent = "Hint isn't available right now. Try again in a moment.";
    } finally {
        hintButton.disabled = false;
        hintButton.textContent = originalLabel;
    }
}

function setupPythonRunner(panel) {
    const runButton = panel.querySelector("[data-run-python]");
    const resetButton = panel.querySelector("[data-reset-python]");
    const hintButton = panel.querySelector("[data-ai-hint]");
    const source = panel.querySelector("[data-python-source]");
    const output = panel.querySelector("[data-python-output]");
    const stdinField = panel.querySelector("[data-python-stdin]");

    if (!runButton || !resetButton || !source || !output) {
        return;
    }

    const initialSource = source.value;
    const initialOutput = output.textContent;

    runButton.addEventListener("click", () => {
        runPython(panel);
    });

    resetButton.addEventListener("click", () => {
        source.value = initialSource;
        output.textContent = initialOutput;
        delete output.dataset.status;
        if (stdinField) {
            stdinField.value = "";
        }
        source.dispatchEvent(new Event("input", { bubbles: true }));
    });

    if (hintButton) {
        hintButton.addEventListener("click", () => {
            requestAiHint(panel);
        });
    }
}

function setupChallengeAutosave(form) {
    const source = form.querySelector("[data-python-source]");
    const status = form.querySelector("[data-autosave-status]");
    const endpoint = form.dataset.autosaveUrl;

    if (!source || !status || !endpoint) {
        return;
    }

    let saveTimeoutId = null;
    let isSaving = false;
    let pendingValue = null;
    let lastSavedValue = source.value;

    async function saveDraft(value) {
        if (isSaving) {
            pendingValue = value;
            return;
        }

        isSaving = true;
        status.textContent = "Saving draft...";

        try {
            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                credentials: "same-origin",
                body: JSON.stringify({ response_text: value }),
            });

            if (!response.ok) {
                throw new Error("Autosave failed.");
            }

            const data = await response.json();
            lastSavedValue = value;
            status.textContent = data.saved_at ? `Draft autosaved ${data.saved_at}.` : "Draft autosaved.";
        } catch (error) {
            status.textContent = "Autosave paused. Use Save Draft to keep your latest changes.";
        } finally {
            isSaving = false;

            if (pendingValue !== null && pendingValue !== lastSavedValue) {
                const nextValue = pendingValue;
                pendingValue = null;
                saveDraft(nextValue);
            } else {
                pendingValue = null;
            }
        }
    }

    source.addEventListener("input", () => {
        if (source.value === lastSavedValue) {
            status.textContent = "Draft matches your last saved version.";
            return;
        }

        status.textContent = "Draft changed. Autosaving soon...";
        window.clearTimeout(saveTimeoutId);
        saveTimeoutId = window.setTimeout(() => {
            saveDraft(source.value);
        }, 1200);
    });
}

function setupQuizExplain(card) {
    const button = card.querySelector("[data-ai-quiz-explain]");
    const output = card.querySelector("[data-ai-quiz-explanation]");

    if (!button || !output) {
        return;
    }

    const endpoint = button.dataset.explainUrl;
    if (!endpoint) {
        return;
    }

    button.addEventListener("click", async () => {
        const lessonSlug = card.dataset.lessonSlug || "";
        const questionIndex = Number.parseInt(card.dataset.questionIndex, 10);
        const selected = card.querySelector('input[type="radio"]:checked');
        const selectedAnswer = selected ? Number.parseInt(selected.value, 10) : null;

        const originalLabel = button.textContent;
        button.disabled = true;
        button.textContent = "Thinking...";
        output.hidden = false;
        output.textContent = "Getting an explanation...";

        try {
            const recaptchaToken = await getRecaptchaToken("ai_quiz_explain");
            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                credentials: "same-origin",
                body: JSON.stringify({
                    lesson_slug: lessonSlug,
                    question_index: questionIndex,
                    selected_answer: selectedAnswer,
                    recaptcha_token: recaptchaToken,
                }),
            });
            const data = await response.json();
            output.textContent = data.ok ? data.explanation : (data.error || "Explanation isn't available right now.");
        } catch (error) {
            output.textContent = "Explanation isn't available right now. Try again in a moment.";
        } finally {
            button.disabled = false;
            button.textContent = originalLabel;
        }
    });
}

function appendChatMessage(container, role, text) {
    const bubble = document.createElement("p");
    bubble.className = `tutor-chat__message tutor-chat__message--${role}`;
    bubble.textContent = text;
    container.appendChild(bubble);
    container.scrollTop = container.scrollHeight;
    return bubble;
}

function setupTutorChat(section) {
    const form = section.querySelector("[data-tutor-chat-form]");
    const input = section.querySelector("[data-tutor-chat-input]");
    const messages = section.querySelector("[data-tutor-chat-messages]");
    const endpoint = section.dataset.chatUrl;
    const lessonSlug = section.dataset.lessonSlug || "";

    if (!form || !input || !messages || !endpoint) {
        return;
    }

    const history = [];

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        const message = input.value.trim();
        if (!message) {
            return;
        }

        appendChatMessage(messages, "user", message);
        input.value = "";
        input.disabled = true;

        const thinkingBubble = appendChatMessage(messages, "assistant", "Thinking...");

        try {
            const recaptchaToken = await getRecaptchaToken("ai_tutor_chat");
            const response = await fetch(endpoint, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                credentials: "same-origin",
                body: JSON.stringify({
                    lesson_slug: lessonSlug,
                    message,
                    history,
                    recaptcha_token: recaptchaToken,
                }),
            });
            const data = await response.json();
            const reply = data.ok ? data.reply : (data.error || "The tutor isn't available right now.");
            thinkingBubble.textContent = reply;
            history.push({ role: "user", content: message });
            history.push({ role: "assistant", content: reply });
        } catch (error) {
            thinkingBubble.textContent = "The tutor isn't available right now. Try again in a moment.";
        } finally {
            input.disabled = false;
            input.focus();
        }
    });
}

function setupNavDropdowns() {
    const dropdowns = document.querySelectorAll(".nav-dropdown");
    if (!dropdowns.length) {
        return;
    }

    dropdowns.forEach((dropdown) => {
        dropdown.addEventListener("toggle", () => {
            if (!dropdown.open) {
                return;
            }

            dropdowns.forEach((other) => {
                if (other !== dropdown && other.open) {
                    other.removeAttribute("open");
                }
            });

            if (dropdown.classList.contains("nav-dropdown--search")) {
                const input = dropdown.querySelector('input[type="search"]');
                if (input) {
                    window.setTimeout(() => input.focus(), 0);
                }
            }
        });
    });

    document.addEventListener("click", (event) => {
        dropdowns.forEach((dropdown) => {
            if (dropdown.open && !dropdown.contains(event.target)) {
                dropdown.removeAttribute("open");
            }
        });
    });
}

function setupClickTracking() {
    document.querySelectorAll("[data-track-click]").forEach((link) => {
        link.addEventListener("click", () => {
            const eventType = link.dataset.trackClick;
            let metadata = {};
            if (link.dataset.trackMetadata) {
                try {
                    metadata = JSON.parse(link.dataset.trackMetadata);
                } catch (error) {
                    metadata = {};
                }
            }
            // A new-tab link leaves the current page intact, so a normal
            // fetch is fine; a same-tab link needs sendBeacon to survive
            // the navigation that starts immediately after this click.
            const opensNewTab = link.target === "_blank";
            trackEngagement(eventType, { metadata, beacon: !opensNewTab });
        });
    });
}

function setupRecaptchaForm(form) {
    form.addEventListener("submit", (event) => {
        if (form.dataset.recaptchaVerified === "true") {
            return;
        }

        event.preventDefault();
        const action = form.dataset.recaptchaAction || "submit";

        getRecaptchaToken(action).then((token) => {
            let field = form.querySelector('input[name="recaptcha_token"]');
            if (!field) {
                field = document.createElement("input");
                field.type = "hidden";
                field.name = "recaptcha_token";
                form.appendChild(field);
            }
            field.value = token || "";
            form.dataset.recaptchaVerified = "true";

            if (form.requestSubmit) {
                form.requestSubmit();
            } else {
                form.submit();
            }
        });
    });
}

function setupTrackedViews() {
    document.querySelectorAll("[data-track-view]").forEach((element) => {
        const eventType = element.dataset.trackView;
        const lessonSlug = element.dataset.lessonSlug || "";
        const dedupeKey = `${eventType}:${lessonSlug}:${window.location.pathname}`;

        if (trackedViews.has(dedupeKey)) {
            return;
        }

        trackedViews.add(dedupeKey);
        trackEngagement(eventType, { lessonSlug });
    });
}

function setupLessonProgressForm(form) {
    const banner = form.closest(".progress-banner");
    const pill = banner ? banner.querySelector("[data-progress-pill]") : null;
    const toast = banner ? banner.querySelector("[data-progress-toast]") : null;
    const actionInput = form.querySelector('input[name="action"]');
    const submitButton = form.querySelector('button[type="submit"]');

    if (!pill || !toast || !actionInput || !submitButton) {
        return;
    }

    // form.action is shadowed by the hidden <input name="action"> below (a
    // named form control shadows the form element's built-in .action
    // property), so the real URL must be read from the content attribute.
    const submitUrl = form.getAttribute("action");
    let toastTimeoutId = null;

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        submitButton.disabled = true;

        try {
            const response = await fetch(submitUrl, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "X-Requested-With": "XMLHttpRequest",
                },
                credentials: "same-origin",
                body: new FormData(form),
            });

            if (!response.ok) {
                throw new Error("Request failed.");
            }

            const data = await response.json();

            if (data.is_completed) {
                pill.textContent = "Completed";
                pill.classList.add("progress-pill--complete");
                actionInput.value = "restart";
                submitButton.textContent = "Reset Lesson";
                submitButton.className = "button button--ghost button--small";
            } else {
                const quizPassed = form.dataset.quizPassed === "true";
                pill.textContent = quizPassed ? "Quiz Passed" : "In Progress";
                pill.classList.toggle("progress-pill--complete", quizPassed);
                actionInput.value = "complete";
                submitButton.textContent = "Mark Complete";
                submitButton.className = "button button--primary button--small";
            }

            if (data.message) {
                toast.textContent = data.message;
                toast.hidden = false;
                window.clearTimeout(toastTimeoutId);
                toastTimeoutId = window.setTimeout(() => {
                    toast.hidden = true;
                }, 4000);
            }
        } catch (error) {
            toast.textContent = "Something went wrong updating your progress. Please try again.";
            toast.hidden = false;
        } finally {
            submitButton.disabled = false;
        }
    });
}

// ── Mini-challenge auto-complete ──────────────────────────────────────────
// When the learner runs their code in the challenge editor, this function
// sends the output to the server, compares it to the expected output, and
// marks the lesson complete on a match, all without a page reload.
function setupMiniChallenge(section) {
    const submitUrl = section.dataset.miniChallengeUrl;
    if (!submitUrl) return;

    const challengePanel = section.querySelector("[data-python-runner][data-runner-mode='challenge']");
    if (!challengePanel) return;

    const runButton = challengePanel.querySelector("[data-run-python]");
    const outputEl = challengePanel.querySelector("[data-python-output]");
    const resultBanner = section.querySelector("[data-challenge-result]");
    const resultMessage = section.querySelector("[data-challenge-result-message]");
    const resultActions = section.querySelector("[data-challenge-result-actions]");

    if (!runButton || !outputEl || !resultBanner || !resultMessage) return;

    // Intercept after Pyodide finishes. We hook a MutationObserver on the
    // output element so we catch the result the moment it is written.
    let lastOutput = "";
    const observer = new MutationObserver(async () => {
        const currentOutput = outputEl.textContent.trim();
        // Skip if output hasn't changed or is still a loading message.
        if (currentOutput === lastOutput || currentOutput === "Loading Python runtime...") return;
        lastOutput = currentOutput;

        // Only submit when the button triggered the run (not reset).
        if (runButton.disabled) return; // still running, so wait

        try {
            const response = await fetch(submitUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
                credentials: "same-origin",
                body: JSON.stringify({ output: currentOutput }),
            });
            const data = await response.json();

            resultBanner.hidden = false;
            resultBanner.classList.toggle("challenge-result--success", !!data.passed);
            resultBanner.classList.toggle("challenge-result--fail", !data.passed);
            resultMessage.textContent = data.message || "";

            if (data.passed && resultActions) {
                resultActions.hidden = false;
            }
        } catch (_err) {
            // Silently skip so the learner can still use the page normally.
        }
    });

    observer.observe(outputEl, { childList: true, subtree: true, characterData: true });
}

document.addEventListener("DOMContentLoaded", () => {
    setupNavDropdowns();
    setupTrackedViews();
    setupClickTracking();
    document.querySelectorAll("[data-python-runner]").forEach(setupPythonRunner);
    document.querySelectorAll("[data-challenge-autosave-form]").forEach(setupChallengeAutosave);
    document.querySelectorAll("[data-lesson-progress-form]").forEach(setupLessonProgressForm);
    document.querySelectorAll("[data-quiz-question]").forEach(setupQuizExplain);
    document.querySelectorAll("[data-tutor-chat]").forEach(setupTutorChat);
    document.querySelectorAll("[data-recaptcha-action]").forEach(setupRecaptchaForm);
    document.querySelectorAll("[data-mini-challenge]").forEach(setupMiniChallenge);
});
