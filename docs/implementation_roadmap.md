# Code with Michael Implementation Roadmap

## Review Summary

The Word document recommends a practice-first beginner Python site with these core ideas:

- Remove setup friction by letting visitors try Python in the browser immediately.
- Make `Start Here` obvious and beginner-safe.
- Structure learning into short modules with one concept per lesson.
- Pair every lesson with a code example, one small modification, a mini challenge, and a short quiz.
- Delay heavy platform work like payments, certificates, and advanced sandboxing until the learning loop is proven.

That guidance fits the current Django repo well if we treat the existing app as the MVP shell instead of rebuilding the stack first.

## Recommended Path For This Repo

### Phase 1: Validate the learning loop

Goal: prove that beginners will land, run code, complete a tiny challenge, and want the next lesson.

Build:

- Home page with a strong beginner promise and a visible `Start Here` path.
- `Start Here`, `Lessons`, `Challenges`, `Projects`, `Tips`, and `Community` pages.
- One fully-formed interactive lesson prototype.
- Static lesson content stored in code so we can move fast before adding CMS models.

Success signals:

- Visitors click through to the first lesson.
- Visitors press `Run Code`.
- Visitors spend time on the page and complete the quiz/challenge.

### Phase 2: Make content manageable

Goal: move from hardcoded content to reusable content records.

Build:

- Django models for modules, lessons, challenges, quizzes, and tips.
- Admin editing flow for lesson content.
- Slug-based routing backed by the database instead of static dictionaries.
- Basic analytics events for lesson views and code runs.

### Phase 3: Add learner retention

Goal: give beginners a reason to come back.

Build:

- Email capture with a real provider integration.
- Optional free accounts for saved progress.
- Continue-learning state and completed lesson tracking.
- Weekly challenge promotion tied to the website content.

### Phase 4: Add social learning loops

Goal: connect the site to the audience you already have.

Build:

- Featured weekly challenge section backed by admin content.
- Learner shoutout or success-story area.
- Discussion prompts or lightweight submissions.

### Phase 5: Monetize carefully

Goal: monetize only after we know what beginners finish.

Build:

- Premium challenge packs or a structured 30-day roadmap.
- Live cohort landing page and checkout flow.
- Downloadables tied to the strongest-performing content themes.

## What Was Built In This Pass

- Replaced the placeholder homepage with a beginner-focused landing page.
- Added the main navigation and core site pages described in the document.
- Added a first interactive lesson prototype with a browser-based Python runner using Pyodide.
- Added a lightweight in-code content layer so the site can grow module-by-module before introducing database models.
- Added Django models, admin registration, and a content service layer for modules, lessons, challenges, projects, tips, and community items.
- Added a starter bootstrap command so the prototype content can be loaded into the database after migrations are run.
- Added first-party engagement tracking for lesson views, quiz views, and code-run attempts so the MVP can measure whether learners are actually using the practice loop.
- Added a staff-only insights page that summarizes engagement totals, lesson-level activity, and recent events.
- Added first-party email capture on the homepage, backed by Django models and admin instead of a third-party provider for the first pass.
- Added a first-pass onboarding email sequence with welcome delivery tracking and a follow-up nudge command.

## Next Build Targets

1. Run migrations and load starter content with `manage.py bootstrap_learning_content`.
2. Expand the first module into 3-5 production-quality lessons.
3. Add learner progress once the content loop is validated.
4. Add trend reporting or date filters for engagement data.
5. Connect onboarding delivery to a real ESP and scheduled automation when you are ready.
