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

async function trackEngagement(eventType, options = {}) {
    const endpoint = document.querySelector('meta[name="engagement-endpoint"]')?.content;
    if (!endpoint) {
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
            body: JSON.stringify({
                event_type: eventType,
                page_path: window.location.pathname,
                lesson_slug: options.lessonSlug || null,
                metadata: options.metadata || {},
            }),
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

function setupPythonRunner(panel) {
    const runButton = panel.querySelector("[data-run-python]");
    const resetButton = panel.querySelector("[data-reset-python]");
    const source = panel.querySelector("[data-python-source]");
    const output = panel.querySelector("[data-python-output]");

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
        source.dispatchEvent(new Event("input", { bubbles: true }));
    });
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

document.addEventListener("DOMContentLoaded", () => {
    setupTrackedViews();
    document.querySelectorAll("[data-python-runner]").forEach(setupPythonRunner);
    document.querySelectorAll("[data-challenge-autosave-form]").forEach(setupChallengeAutosave);
});
