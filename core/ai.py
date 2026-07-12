import logging

import anthropic
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger('django')

MODEL = 'claude-opus-4-8'
FALLBACK_MESSAGE = "AI help isn't available right now. Try again in a moment."

_client = None


def get_client():
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    return _client


def check_rate_limit(request, feature, limit=10, window_seconds=3600):
    if request.user.is_authenticated:
        identity = f'user:{request.user.pk}'
    else:
        if not request.session.session_key:
            request.session.create()
        identity = f'session:{request.session.session_key}'

    key = f'ai_rate:{feature}:{identity}'
    count = cache.get(key)
    if count is None:
        cache.set(key, 1, timeout=window_seconds)
        return False
    if count >= limit:
        return True
    try:
        cache.incr(key)
    except ValueError:
        cache.set(key, 1, timeout=window_seconds)
    return False


def _complete(system, messages, max_tokens=500):
    try:
        response = get_client().messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=system,
            thinking={'type': 'adaptive'},
            output_config={'effort': 'low'},
            messages=messages,
        )
    except Exception:
        logger.exception('Anthropic API call failed')
        return FALLBACK_MESSAGE

    text = next((block.text for block in response.content if block.type == 'text'), '')
    return text.strip() or FALLBACK_MESSAGE


CODE_HINT_SYSTEM = (
    "You are a friendly, encouraging Python tutor for absolute beginners on a site called "
    "Code with Michael. A learner is working through a lesson or challenge and ran their code. "
    "Give a short hint (2-4 sentences, plain English, no jargon) that helps them understand "
    "what happened and nudges them toward the fix themselves. Do not just hand them corrected "
    "code unless the fix is a single small change. Be warm, never condescending."
)


def get_code_hint(*, title, goal, code, output, is_error):
    user_content = (
        f"Title: {title}\n"
        f"Goal/prompt: {goal}\n\n"
        f"Learner's code:\n{code}\n\n"
        f"{'Error' if is_error else 'Output'}:\n{output or '(no output yet)'}\n\n"
        "Give the learner a short hint."
    )
    return _complete(CODE_HINT_SYSTEM, [{'role': 'user', 'content': user_content}], max_tokens=400)


QUIZ_EXPLANATION_SYSTEM = (
    "You are a friendly Python tutor for absolute beginners on a site called Code with Michael. "
    "Explain quiz answers in plain English in 2-4 sentences. Be encouraging, never condescending."
)


def get_quiz_explanation(*, question, options, correct_answer, selected_answer):
    options_text = '\n'.join(f'{i}. {opt}' for i, opt in enumerate(options))
    correct_text = options[correct_answer] if isinstance(correct_answer, int) and 0 <= correct_answer < len(options) else 'Unknown'
    selected_text = (
        options[selected_answer]
        if isinstance(selected_answer, int) and 0 <= selected_answer < len(options)
        else 'No answer selected'
    )
    user_content = (
        f"Question: {question}\n"
        f"Options:\n{options_text}\n\n"
        f"Correct answer: {correct_text}\n"
        f"Learner's answer: {selected_text}\n\n"
        "Explain why the correct answer is right. If the learner's answer was wrong, briefly "
        "explain the misconception behind it."
    )
    return _complete(QUIZ_EXPLANATION_SYSTEM, [{'role': 'user', 'content': user_content}], max_tokens=400)


TUTOR_CHAT_SYSTEM_TEMPLATE = (
    "You are a friendly Python tutor for absolute beginners on a site called Code with Michael. "
    "The learner is currently on the lesson '{title}': {summary}\n\n"
    "Lesson content for reference:\n{explanation}\n\n"
    "Answer the learner's questions about this lesson in plain English. Keep answers short "
    "(under 150 words) unless a code example is genuinely needed. Stay focused on this lesson's "
    "topic; if asked something unrelated to Python or this lesson, gently redirect."
)


def get_tutor_reply(*, lesson_title, lesson_summary, lesson_explanation, history, message):
    system = TUTOR_CHAT_SYSTEM_TEMPLATE.format(
        title=lesson_title or 'Python practice',
        summary=lesson_summary or '',
        explanation=lesson_explanation or '',
    )
    messages = []
    for turn in history[-8:]:
        role = turn.get('role') if isinstance(turn, dict) else None
        content = turn.get('content') if isinstance(turn, dict) else None
        if role in ('user', 'assistant') and content:
            messages.append({'role': role, 'content': str(content)[:2000]})
    messages.append({'role': 'user', 'content': message[:2000]})
    return _complete(system, messages, max_tokens=600)
