SITE_STATS = {
    'followers': '4,500+',
    'lesson_count': 14,
    'challenge_count': 14,
    'quiz_count': 5,
}

HOME_FEATURES = [
    {
        'title': 'Start coding in under a minute',
        'description': 'The first lesson opens with runnable Python right in the browser, so beginners can learn without setup stress.',
    },
    {
        'title': 'One idea at a time',
        'description': 'Each lesson teaches a single concept, gives a tiny win, and explains common mistakes in plain English.',
    },
    {
        'title': 'Practice before perfection',
        'description': 'Challenges, expected output, and quick quizzes help learners build confidence before moving on.',
    },
]

ROADMAP_STEPS = [
    {'label': 'Basics', 'description': 'print(), comments, variables, and the first small wins.'},
    {'label': 'Practice', 'description': 'Short challenges that ask learners to change one thing and rerun it.'},
    {'label': 'Projects', 'description': 'Mini apps like a tip calculator, quiz game, and budget tracker.'},
    {'label': 'Confidence', 'description': 'Debugging habits, repeat practice, and a clear next-step path.'},
]

NAV_PAGES = [
    {'title': 'Start Here', 'url_name': 'core:start_here', 'description': 'A guided first step for absolute beginners.'},
    {'title': 'Lessons', 'url_name': 'core:lessons', 'description': 'Short concepts with examples, challenges, and quizzes.'},
    {'title': 'Challenges', 'url_name': 'core:challenges', 'description': 'Practice cards with hints and expected output.'},
]

NAV_PAGES_MORE = [
    {'title': 'Projects', 'url_name': 'core:projects', 'description': 'Mini builds that combine multiple beginner skills.'},
    {'title': 'Tips', 'url_name': 'core:tips', 'description': 'Quick wins and common-mistake fixes from your social content.'},
    {'title': 'Community', 'url_name': 'core:community', 'description': 'Weekly prompts and learner shoutouts connected to your audience.'},
    {'title': 'Full Course', 'url_name': 'core:premium_course', 'description': 'The complete Python for Absolute Beginners course, unlocked with a one-time purchase.'},
]

# TODO: replace with your real profile URLs.
SOCIAL_LINKS = [
    {'label': 'Facebook', 'icon': 'bi-facebook', 'url': 'https://www.facebook.com/profile.php?id=61589092320241'},
    {'label': 'Instagram', 'icon': 'bi-instagram', 'url': 'https://www.instagram.com/code_with_michael/'},
    {'label': 'Threads', 'icon': 'bi-threads', 'url': 'https://www.threads.com/@code_with_michael'},
]

MODULES = [
    {
        'number': 1,
        'slug': 'first-steps',
        'title': 'First Steps',
        'duration': '10 min',
        'goal': 'Run your first Python code and learn what print() does.',
        'topics': ['print()', 'common beginner mistakes'],
    },
    {
        'number': 2,
        'slug': 'variables-and-data-types',
        'title': 'Variables and Data Types',
        'duration': '12 min',
        'goal': 'Store text and numbers in variables and use names that make sense.',
        'topics': ['variables', 'strings', 'f-strings', 'integers and floats'],
    },
    {
        'number': 3,
        'slug': 'input-and-output',
        'title': 'Input and Output',
        'duration': '12 min',
        'goal': 'Collect user input and format friendly responses with f-strings.',
        'topics': ['input()', 'converting text to numbers', 'f-strings with input'],
    },
    {
        'number': 4,
        'slug': 'decisions',
        'title': 'Decisions',
        'duration': '14 min',
        'goal': 'Understand booleans, then choose different actions with if, elif, and else.',
        'topics': ['booleans', 'if', 'elif', 'else', 'comparison operators'],
    },
    {
        'number': 5,
        'slug': 'collections-and-loops',
        'title': 'Collections and Loops',
        'duration': '40 min',
        'goal': 'Store values in lists, dictionaries, tuples, and sets, then use loops to work through them.',
        'topics': ['lists', 'dictionaries', 'indexing', 'for loops', 'tuples', 'sets'],
    },
    {
        'number': 6,
        'slug': 'functions',
        'title': 'Functions',
        'duration': '15 min',
        'goal': 'Create reusable code with parameters and return values.',
        'topics': ['def', 'parameters', 'return', 'reuse'],
    },
    {
        'number': 7,
        'slug': 'debugging-basics',
        'title': 'Debugging Basics',
        'duration': '12 min',
        'goal': 'Read errors calmly and use print debugging to find what changed.',
        'topics': ['tracebacks', 'print debugging', 'TypeError'],
    },
    {
        'number': 8,
        'slug': 'error-handling',
        'title': 'Error Handling',
        'duration': '12 min',
        'goal': 'Catch problems with try and except instead of letting your program crash.',
        'topics': ['try', 'except', 'catching specific errors'],
    },
    {
        'number': 9,
        'slug': 'working-with-files',
        'title': 'Working with Files',
        'duration': '12 min',
        'goal': 'Save data that sticks around by reading and writing simple text files.',
        'topics': ['open()', 'with blocks', 'reading a file', 'writing a file'],
    },
    {
        'number': 10,
        'slug': 'modules-and-libraries',
        'title': 'Modules and Libraries',
        'duration': '10 min',
        'goal': "Use Python's built-in toolbox instead of writing everything from scratch.",
        'topics': ['import', 'built-in modules', 'random', 'reproducible randomness'],
    },
    {
        'number': 11,
        'slug': 'intro-to-classes',
        'title': 'Introduction to Classes and Objects',
        'duration': '14 min',
        'goal': 'Understand the basics of bundling data and behavior together with a class.',
        'topics': ['class', '__init__', 'attributes', 'methods', 'instances'],
    },
    {
        'number': 12,
        'slug': 'mini-projects',
        'title': 'Mini Projects',
        'duration': '20 min',
        'goal': 'Combine input, conditionals, and f-strings into one small, complete program.',
        'topics': ['combining input and conditionals', 'planning in plain English', 'a simple budget program'],
    },
    {
        'number': 13,
        'slug': 'next-steps',
        'title': 'Next Steps',
        'duration': '10 min',
        'goal': 'Prepare to install Python locally and keep building after the browser lessons.',
        'topics': ['installing Python locally', 'a code editor', 'running a .py file', 'choosing your next goal'],
    },
]

LESSONS = [
    {
        'slug': 'print-basics',
        'module_slug': 'first-steps',
        'title': 'Your First Python Output',
        'summary': 'Run print() for the first time and change one line to make it your own.',
        'duration': '8 min',
        'goal': 'By the end, you will know how to use print() to display text on the screen.',
        'explanation': 'print() tells Python to show something in the output area. It is one of the fastest ways to get an immediate win because you can run one line and see a result right away.',
        'starter_code': 'print("Hello from Code_with_Michael!")\nprint("I am learning Python one step at a time.")',
        'try_it': 'Change the second line so it says your name and one reason you want to learn Python.',
        'common_mistake': 'Forgetting the closing quote or parenthesis causes a syntax error. If Python says a string was never closed, check the line above the error first.',
        'mini_challenge': 'Use print() three times to produce this exact output:\nLearning Python\nLine by line\nI can do this',
        'challenge_starter_code': '# Use print() three times to produce the exact output shown in the challenge.\n# Line 1: Learning Python\n# Line 2: Line by line\n# Line 3: I can do this\n',
        'challenge_expected_output': 'Learning Python\nLine by line\nI can do this',
        'expected_output': 'Hello from Code_with_Michael!\nI am learning Python one step at a time.',
        'practice_challenge_slug': 'warm-up-greeting',
        'quiz': [
            {
                'question': 'What does print() do?',
                'options': [
                    'It shows text or values in the output area.',
                    'It saves code to your computer.',
                    'It asks the user a question.',
                ],
                'answer': 0,
                'explanation': 'print() displays something so the learner can immediately see what the code produced.',
            },
            {
                'question': 'Which line is valid Python?',
                'options': [
                    'print("Hello")',
                    'print("Hello"',
                    'print Hello',
                ],
                'answer': 0,
                'explanation': 'Python needs matching quotes and parentheses around the value passed to print().',
            },
            {
                'question': 'Why is print() a good first lesson?',
                'options': [
                    'It gives instant feedback with very little code.',
                    'It installs Python for you.',
                    'It only works in advanced projects.',
                ],
                'answer': 0,
                'explanation': 'Beginners build confidence faster when they can run one line and see the result right away.',
            },
        ],
    },
    {
        'slug': 'variables-basics',
        'module_slug': 'variables-and-data-types',
        'title': 'Variables: Naming and Storing Information',
        'summary': 'Learn what a variable is, why names matter, and how Python stores values for you to reuse later.',
        'duration': '10 min',
        'goal': 'By the end, you will know how to create variables, update them, and choose beginner-friendly names.',
        'explanation': (
            'A variable is just a named place to store a value. Instead of writing the same value over and over, you give it a clear name and reuse it later.\n\n'
            'Variables help your code stay readable. Compare player_score = 12 with x = 12. Both work, but one makes your intention much clearer.\n\n'
            'This lesson is about building the habit of naming things well and updating values on purpose.'
        ),
        'starter_code': (
            'student_name = "Michael"\n'
            'practice_goal = "Finish one Python lesson"\n'
            'practice_days = 3\n'
            '\n'
            'print(student_name)\n'
            'print(practice_goal)\n'
            'print(practice_days)\n'
            '\n'
            'practice_days = practice_days + 2\n'
            'print(practice_days)'
        ),
        'try_it': (
            'Change the variable values to match your own learning situation.\n'
            '- Put your own name in student_name.\n'
            '- Change practice_goal to something you want to accomplish.\n'
            '- Change practice_days to a different number.\n'
            '- Then change practice_days again by adding 1 instead of 2.'
        ),
        'common_mistake': (
            'A common beginner mistake is using a variable name before creating it. Python cannot print player_name if you never assigned a value to player_name first.\n\n'
            'Another mistake is choosing names that are too vague. A name like goal_score is much easier to understand than a single letter like g.'
        ),
        'mini_challenge': 'Create a variable called sessions set to 3 and print it. Then add 2 to sessions and print it again. Expected output: 3 then 5.',
        'challenge_starter_code': '# 1. Create a variable called sessions and set it to 3\n# 2. Print sessions\n# 3. Add 2 to sessions\n# 4. Print sessions again\n',
        'challenge_expected_output': '3\n5',
        'expected_output': 'Michael\nFinish one Python lesson\n3\n5',
        'practice_challenge_slug': 'simple-scoreboard',
        'quiz': [
            {
                'question': 'What is a variable?',
                'options': [
                    'A named place to store a value.',
                    'A special kind of loop.',
                    'A Python error message.',
                ],
                'answer': 0,
                'explanation': 'Variables let you give a value a name so you can reuse it later.',
            },
            {
                'question': 'Why is player_score a better variable name than x?',
                'options': [
                    'It makes the purpose of the value clearer.',
                    'It makes Python run faster every time.',
                    'It turns every value into a string.',
                ],
                'answer': 0,
                'explanation': 'Good names make code easier to understand for both you and future readers.',
            },
            {
                'question': 'What happens when you assign a new value to an existing variable?',
                'options': [
                    'The variable now stores the new value.',
                    'Python creates a syntax error automatically.',
                    'The old value and new value combine into a list.',
                ],
                'answer': 0,
                'explanation': 'Variables are meant to be updated when your data changes.',
            },
        ],
    },
    {
        'slug': 'strings-and-fstrings',
        'module_slug': 'variables-and-data-types',
        'title': 'Strings and F-Strings',
        'summary': 'Work with text in Python and learn how f-strings make output easier to read.',
        'duration': '12 min',
        'goal': 'By the end, you will know how to create strings, combine text, and use f-strings to build clear output.',
        'explanation': (
            'Strings are pieces of text wrapped in quotes. They can store names, messages, labels, and almost anything you want to display.\n\n'
            'F-strings are one of the easiest ways to mix text with variables. Instead of trying to glue strings together awkwardly, you can write one readable sentence and place variables directly inside it.'
        ),
        'starter_code': (
            'student_name = "Michael"\n'
            'favorite_language = "Python"\n'
            'current_goal = "build beginner lessons"\n'
            '\n'
            'print(student_name)\n'
            'print("Favorite language: " + favorite_language)\n'
            'print(f"{student_name} wants to {current_goal} with {favorite_language}.")'
        ),
        'try_it': 'Replace the three string values with your own information.\nThen create one more f-string sentence that shares what you want to build or learn next.',
        'common_mistake': 'The most common string mistake is forgetting matching quotes.\n\nA common f-string mistake is forgetting the `f` before the opening quote. Without it, Python prints the braces instead of the variable values.',
        'mini_challenge': 'Using the two variables provided, print one f-string sentence that reads exactly: Alex wants to learn loops.',
        'challenge_starter_code': 'name = "Alex"\ngoal = "learn loops"\n# Print one sentence using an f-string so the output reads:\n# Alex wants to learn loops.\n',
        'challenge_expected_output': 'Alex wants to learn loops.',
        'expected_output': 'Michael\nFavorite language: Python\nMichael wants to build beginner lessons with Python.',
        'practice_challenge_slug': 'mood-check',
        'quiz': [
            {
                'question': 'Which value is a string?',
                'options': ['"Python"', '3.14', 'True'],
                'answer': 0,
                'explanation': 'Strings use quotes because they represent text.',
            },
            {
                'question': 'What is the benefit of an f-string?',
                'options': [
                    'It places variables inside readable text.',
                    'It removes the need for variables.',
                    'It automatically creates functions.',
                ],
                'answer': 0,
                'explanation': 'F-strings make text output cleaner and easier to build.',
            },
            {
                'question': 'Why does `print("{name}")` not show the value of name?',
                'options': [
                    'Because it is missing the `f` before the string.',
                    'Because braces are not allowed in Python.',
                    'Because strings cannot contain variables.',
                ],
                'answer': 0,
                'explanation': 'The `f` tells Python to treat braces as variable placeholders.',
            },
        ],
    },
    {
        'slug': 'ints-and-floats',
        'module_slug': 'variables-and-data-types',
        'title': 'Integers and Floats',
        'summary': 'Learn the difference between whole numbers and decimal numbers and use them in simple calculations.',
        'duration': '12 min',
        'goal': 'By the end, you will know when to use ints, when to use floats, and how to do basic math with both.',
        'explanation': (
            'Integers are whole numbers like 3, 10, or 42. Floats are numbers with decimals like 1.5, 9.99, or 100.0.\n\n'
            'Both are useful, but they often show up in different situations. A quantity of books is usually an int. A price, average, or percentage is often a float.'
        ),
        'starter_code': (
            'completed_lessons = 4\n'
            'study_hours = 2.5\n'
            'bonus_hours = 1.0\n'
            '\n'
            'total_hours = study_hours + bonus_hours\n'
            'double_lessons = completed_lessons * 2\n'
            '\n'
            'print(completed_lessons)\n'
            'print(total_hours)\n'
            'print(double_lessons)'
        ),
        'try_it': 'Change completed_lessons to a different whole number and change study_hours to a different decimal number.\nThen create one more variable called average_hours and set it to total_hours / 2.',
        'common_mistake': 'A common mistake is putting quotes around numbers. "5" looks like a number, but Python treats it as text if it has quotes.\n\nAnother mistake is expecting every calculation to stay a whole number. Division often produces a float.',
        'mini_challenge': 'Print sessions on the first line, then print the total hours (sessions times hours_each) on the second line. Expected output: 4 then 6.0.',
        'challenge_starter_code': 'sessions = 4\nhours_each = 1.5\n# Print sessions on the first line.\n# Print the total hours (sessions times hours_each) on the second line.\n',
        'challenge_expected_output': '4\n6.0',
        'expected_output': '4\n3.5\n8',
        'practice_challenge_slug': 'data-type-mix-up',
        'quiz': [
            {
                'question': 'Which value is a float?',
                'options': ['2.75', '7', '"2.75"'],
                'answer': 0,
                'explanation': 'A float includes a decimal point and is not wrapped in quotes.',
            },
            {
                'question': 'Which value is best stored as an int?',
                'options': [
                    'The number of lessons completed',
                    'The price of a coffee',
                    'The average speed in miles per hour',
                ],
                'answer': 0,
                'explanation': 'Counts are usually whole numbers, so ints are a natural fit.',
            },
            {
                'question': 'What happens when you divide numbers in Python?',
                'options': [
                    'The result is often a float.',
                    'The result is always a string.',
                    'The result can never include decimals.',
                ],
                'answer': 0,
                'explanation': 'Division commonly produces a decimal result, so floats appear naturally.',
            },
        ],
    },
    {
        'slug': 'booleans-and-choices',
        'module_slug': 'decisions',
        'title': 'Booleans and Simple Decisions',
        'summary': 'Use True and False values to represent conditions and drive simple decision-making.',
        'duration': '12 min',
        'goal': 'By the end, you will know what booleans are and how to use them in simple if statements.',
        'explanation': (
            'A boolean has only two possible values: True or False. Booleans are helpful whenever you want to track whether something is happening, has happened, or should happen.\n\n'
            'They become especially useful when you pair them with if statements to make simple choices in your code.'
        ),
        'starter_code': (
            'finished_lesson = True\n'
            'needs_review = False\n'
            '\n'
            'if finished_lesson:\n'
            '    print("Great job finishing the lesson.")\n'
            '\n'
            'if not needs_review:\n'
            '    print("You are ready for the next step.")'
        ),
        'try_it': 'Change finished_lesson to False and run the code again.\nThen change needs_review to True and notice what changes in the output.',
        'common_mistake': 'Python booleans are written as True and False with capital letters. Writing true or false causes an error because Python looks for variable names with those spellings.',
        'mini_challenge': 'Use if and else on practiced_today. If it is True print: Nice work today. Otherwise print: Try again tomorrow.',
        'challenge_starter_code': 'practiced_today = True\n# Use if and else.\n# If practiced_today is True, print: Nice work today.\n# Otherwise print: Try again tomorrow.\n',
        'challenge_expected_output': 'Nice work today.',
        'expected_output': 'Great job finishing the lesson.\nYou are ready for the next step.',
        'practice_challenge_slug': 'boolean-checkpoint',
        'quiz': [
            {
                'question': 'Which option is a valid boolean value in Python?',
                'options': ['True', '"True"', 'yes'],
                'answer': 0,
                'explanation': 'True is the actual boolean value. "True" is only a string.',
            },
            {
                'question': 'Why are booleans useful?',
                'options': [
                    'They help represent whether something is true or false.',
                    'They replace every number in Python.',
                    'They are only used inside strings.',
                ],
                'answer': 0,
                'explanation': 'Booleans let you track conditions and make decisions in code.',
            },
            {
                'question': 'What does `if finished_lesson:` mean?',
                'options': [
                    'Run the indented code only if finished_lesson is True.',
                    'Turn finished_lesson into a string.',
                    'Create a new variable automatically.',
                ],
                'answer': 0,
                'explanation': 'If statements check conditions before running code.',
            },
        ],
    },
    {
        'slug': 'conditionals-basics',
        'module_slug': 'decisions',
        'title': 'Conditionals with if, elif, and else',
        'summary': 'Use conditionals to make Python choose between different actions based on changing values.',
        'duration': '14 min',
        'goal': 'By the end, you will know how to use if, elif, and else to make simple decisions in your programs.',
        'explanation': (
            'Conditionals help your program react to different situations. Instead of always printing the same result, you can ask Python to check a condition first.\n\n'
            'An if block runs when the condition is true. An elif block gives you another condition to check. An else block catches everything that did not match the earlier checks.\n\n'
            'This is where your code starts to feel more interactive and more useful.'
        ),
        'starter_code': (
            'score = 82\n'
            '\n'
            'if score >= 90:\n'
            '    print("Excellent work.")\n'
            'elif score >= 70:\n'
            '    print("Nice job. Keep practicing.")\n'
            'else:\n'
            '    print("Keep going. One more practice round will help.")'
        ),
        'try_it': 'Change score to a value above 90, then to a value below 70.\nWatch how Python chooses a different branch each time.',
        'common_mistake': 'A common mistake is writing the conditions out of order. If you check a lower threshold first, Python may never reach the later condition you intended.\n\nAnother common mistake is forgetting the colon after if, elif, or else.',
        'mini_challenge': 'Use if, elif, and else on temperature. 85 or higher prints Hot, 60 to 84 prints Mild, below 60 prints Cold. Expected output: Mild.',
        'challenge_starter_code': 'temperature = 75\n# Use if, elif, and else.\n# 85 or higher prints: Hot\n# 60 to 84 prints: Mild\n# below 60 prints: Cold\n',
        'challenge_expected_output': 'Mild',
        'expected_output': 'Nice job. Keep practicing.',
        'practice_challenge_slug': 'conditional-coach',
        'quiz': [
            {
                'question': 'When does an if block run?',
                'options': [
                    'When its condition is true.',
                    'Every time no matter what.',
                    'Only after a loop finishes.',
                ],
                'answer': 0,
                'explanation': 'If blocks run only when their condition evaluates to true.',
            },
            {
                'question': 'Why use elif?',
                'options': [
                    'To check another condition if the first one was false.',
                    'To replace every boolean in your program.',
                    'To automatically print all results at once.',
                ],
                'answer': 0,
                'explanation': 'Elif gives you another branch to test after the first condition fails.',
            },
            {
                'question': 'What is the role of else?',
                'options': [
                    'It handles the remaining case when earlier conditions do not match.',
                    'It creates a variable named else.',
                    'It only works inside functions.',
                ],
                'answer': 0,
                'explanation': 'Else acts as the fallback branch when the earlier conditions are false.',
            },
        ],
    },
    {
        'slug': 'lists-and-dictionaries-basics',
        'module_slug': 'collections-and-loops',
        'title': 'Lists and Dictionaries',
        'summary': 'Store grouped values in lists and pair labels with values in dictionaries.',
        'duration': '15 min',
        'goal': 'By the end, you will know when to use a list, when to use a dictionary, and how to read values from both.',
        'explanation': (
            'Lists help you store multiple items in order. They are great when you want to keep a sequence of values like lesson names, scores, or goals.\n\n'
            'Dictionaries help you match labels to values. They are useful when each piece of information has a name, like {"name": "Michael", "goal": "Practice Python"}.\n\n'
            'Once you understand lists and dictionaries, your programs become much better at organizing real information.'
        ),
        'starter_code': (
            'practice_topics = ["variables", "strings", "loops"]\n'
            'student_profile = {\n'
            '    "name": "Michael",\n'
            '    "goal": "Finish the beginner path",\n'
            '    "days_practiced": 4,\n'
            '}\n'
            '\n'
            'print(practice_topics[0])\n'
            'print(student_profile["name"])\n'
            'print(student_profile["goal"])'
        ),
        'try_it': 'Add one more topic to the list.\nThen change the dictionary values so they match your own name, goal, and practice count.',
        'common_mistake': 'A common list mistake is trying to access an index that does not exist.\n\nA common dictionary mistake is misspelling a key. If the dictionary uses "name", then "Name" or "student_name" is not the same key.',
        'mini_challenge': 'Print the second item in goals, then the name value and the topic value from profile. Expected output: code, Sam, lists.',
        'challenge_starter_code': 'goals = ["read", "code", "rest"]\nprofile = {"name": "Sam", "topic": "lists"}\n# Print the second item in goals.\n# Print the name value from profile.\n# Print the topic value from profile.\n',
        'challenge_expected_output': 'code\nSam\nlists',
        'expected_output': 'variables\nMichael\nFinish the beginner path',
        'practice_challenge_slug': 'list-and-dictionary-snapshot',
        'quiz': [
            {
                'question': 'When is a list useful?',
                'options': [
                    'When you want to store multiple items in order.',
                    'When you only want true or false values.',
                    'When you want duplicates removed automatically every time.',
                ],
                'answer': 0,
                'explanation': 'Lists are good for ordered groups of values.',
            },
            {
                'question': 'What makes a dictionary different from a list?',
                'options': [
                    'A dictionary uses keys to label values.',
                    'A dictionary can only store numbers.',
                    'A dictionary cannot store strings.',
                ],
                'answer': 0,
                'explanation': 'Dictionaries match labels, called keys, to values.',
            },
            {
                'question': 'How do you read the name from `student_profile = {"name": "Michael"}`?',
                'options': [
                    'student_profile["name"]',
                    'student_profile[0]',
                    'student_profile.name()',
                ],
                'answer': 0,
                'explanation': 'You use the key inside square brackets to get the matching value.',
            },
        ],
    },
    {
        'slug': 'loops-in-action',
        'module_slug': 'collections-and-loops',
        'title': 'Loops in Action',
        'summary': 'Use loops to repeat work cleanly instead of copying the same print statements over and over.',
        'duration': '14 min',
        'goal': 'By the end, you will know how a for loop repeats actions for each item in a group.',
        'explanation': (
            'Loops help you repeat work without writing the same line again and again. A for loop is perfect when you already have a group of items and want to do something with each one.\n\n'
            'This makes your code shorter, cleaner, and easier to update later.'
        ),
        'starter_code': (
            'practice_topics = ["variables", "strings", "loops"]\n'
            '\n'
            'for topic in practice_topics:\n'
            '    print(f"Today I practiced: {topic}")'
        ),
        'try_it': 'Add one or two more topics to the list and run the loop again.\nThen change the sentence inside print() so it sounds more like your own voice.',
        'common_mistake': 'A missing colon after the for line or bad indentation on the next line causes many beginner loop errors. If the loop is not working, check the colon and indentation first.',
        'mini_challenge': "Use a for loop to print each goal with the prefix 'Goal: '. Expected output: Goal: read, Goal: code, Goal: rest.",
        'challenge_starter_code': 'goals = ["read", "code", "rest"]\n# Use a for loop to print each goal with the prefix "Goal: "\n# Example first line: Goal: read\n',
        'challenge_expected_output': 'Goal: read\nGoal: code\nGoal: rest',
        'expected_output': 'Today I practiced: variables\nToday I practiced: strings\nToday I practiced: loops',
        'practice_challenge_slug': 'loop-through-a-list',
        'quiz': [
            {
                'question': 'Why use a loop?',
                'options': [
                    'To repeat an action for multiple items.',
                    'To turn every value into a boolean.',
                    'To replace all variables with strings.',
                ],
                'answer': 0,
                'explanation': 'Loops save time and reduce repeated code.',
            },
            {
                'question': 'What does `topic` represent in `for topic in practice_topics`?',
                'options': [
                    'The current item being processed in the loop.',
                    'The whole list forever.',
                    'A built-in Python keyword you cannot rename.',
                ],
                'answer': 0,
                'explanation': 'The loop variable holds one item at a time as Python moves through the collection.',
            },
            {
                'question': 'What punctuation is required at the end of a for loop line?',
                'options': ['A colon', 'A comma', 'A semicolon'],
                'answer': 0,
                'explanation': 'Python uses a colon to begin the indented block for a loop.',
            },
        ],
    },
    {
        'slug': 'tuples-and-sets',
        'module_slug': 'collections-and-loops',
        'title': 'Tuples and Sets',
        'summary': 'Learn when to group fixed values in a tuple and when to use a set to keep only unique values.',
        'duration': '14 min',
        'goal': 'By the end, you will understand the basic purpose of tuples and sets and know when each one is useful.',
        'explanation': (
            'Tuples and sets both group values together, but they solve different problems.\n\n'
            'A tuple is useful when you want a fixed collection that should stay in that exact grouping. A set is useful when you only care about unique values and do not want duplicates.'
        ),
        'starter_code': (
            'favorite_topics = ("variables", "strings", "functions")\n'
            'completed_topics = {"variables", "strings", "strings", "loops"}\n'
            '\n'
            'print(favorite_topics)\n'
            'print(completed_topics)\n'
            '\n'
            'for topic in favorite_topics:\n'
            '    print(f"Favorite topic: {topic}")'
        ),
        'try_it': 'Change the tuple to your own three favorite topics.\nThen add repeated items to the set and notice that duplicates do not stay there.',
        'common_mistake': 'Beginners sometimes expect sets to preserve duplicates or a predictable printed order. Sets focus on uniqueness, not on keeping repeated items.',
        'mini_challenge': 'Print how many items are in colors, then use a for loop to print each color on its own line. Expected output: 3, red, green, blue.',
        'challenge_starter_code': 'colors = ("red", "green", "blue")\n# Print how many items are in colors.\n# Then use a for loop to print each color on its own line.\n',
        'challenge_expected_output': '3\nred\ngreen\nblue',
        'expected_output': "('variables', 'strings', 'functions')\n{'variables', 'strings', 'loops'} (the order of items in a set can vary, so yours may not match exactly)\nFavorite topic: variables\nFavorite topic: strings\nFavorite topic: functions",
        'practice_challenge_slug': 'tuple-to-loop',
        'quiz': [
            {
                'question': 'When is a tuple useful?',
                'options': [
                    'When you want to keep a fixed grouped collection.',
                    'When you need key-value pairs.',
                    'When you want duplicate values to be stored many times.',
                ],
                'answer': 0,
                'explanation': 'Tuples are a simple way to group related values together.',
            },
            {
                'question': 'Why use a set?',
                'options': [
                    'To keep unique values and ignore duplicates.',
                    'To automatically sort numbers from low to high.',
                    'To replace every loop in your code.',
                ],
                'answer': 0,
                'explanation': 'Sets are strongest when uniqueness matters more than order.',
            },
            {
                'question': 'What happens if you put the same string into a set more than once?',
                'options': [
                    'The set keeps only one copy of it.',
                    'The set stores every duplicate separately.',
                    'Python throws a syntax error immediately.',
                ],
                'answer': 0,
                'explanation': 'Sets remove duplicates by design.',
            },
        ],
    },
    {
        'slug': 'functions-basics',
        'module_slug': 'functions',
        'title': 'Functions: Reusable Blocks of Code',
        'summary': 'Write your first function so repeated code becomes a reusable tool instead of copied lines.',
        'duration': '15 min',
        'goal': 'By the end, you will know how to define a simple function, pass it values, and return a result.',
        'explanation': (
            'Functions help you package logic into a named block you can reuse. Instead of rewriting the same code every time, you define it once and call it whenever you need it.\n\n'
            'This keeps code cleaner and prepares you for bigger projects where repetition quickly becomes messy.'
        ),
        'starter_code': (
            'def introduce_student(name, focus_topic):\n'
            '    return f"{name} is practicing {focus_topic} today."\n'
            '\n'
            'message = introduce_student("Michael", "functions")\n'
            'print(message)'
        ),
        'try_it': 'Call the function with your own name and a different topic.\nThen create a second call with another person or another topic to prove the function can be reused.',
        'common_mistake': 'One of the most common beginner mistakes is forgetting the colon after the function line or forgetting to indent the code inside the function.\n\nAnother is defining a function but never calling it, which makes it look like nothing happened.',
        'mini_challenge': 'Write a function called double that takes one number and returns it times 2. Print the result of calling double(6). Expected output: 12.',
        'challenge_starter_code': '# Write a function called double that takes one number and returns it times 2.\n# Then print the result of calling double(6).\n',
        'challenge_expected_output': '12',
        'expected_output': 'Michael is practicing functions today.',
        'practice_challenge_slug': 'function-practice',
        'quiz': [
            {
                'question': 'Why use a function?',
                'options': [
                    'To reuse logic without copying the same code repeatedly.',
                    'To turn every value into a tuple.',
                    'To avoid using variables.',
                ],
                'answer': 0,
                'explanation': 'Functions reduce repetition and keep logic organized.',
            },
            {
                'question': 'What do the values inside the parentheses in a function definition represent?',
                'options': [
                    'Parameters the function can use.',
                    'A required loop.',
                    'A list of Python errors.',
                ],
                'answer': 0,
                'explanation': 'Parameters let a function receive values when it is called.',
            },
            {
                'question': 'What does `return` do?',
                'options': [
                    'It sends a result back from the function.',
                    'It repeats the function forever.',
                    'It creates a new loop automatically.',
                ],
                'answer': 0,
                'explanation': 'Return gives the function\'s result back to the place where it was called.',
            },
        ],
    },
    {
        'slug': 'error-handling-basics',
        'module_slug': 'error-handling',
        'title': 'Handling Errors with try and except',
        'summary': 'Stop a bad value from crashing your program — catch errors gracefully with try and except.',
        'duration': '12 min',
        'goal': 'By the end, you will know how to use try and except to handle an error instead of letting your program crash.',
        'explanation': (
            'So far, whenever something has gone wrong in your code, Python has printed a red error message and stopped completely. That is fine while you are learning, but a real program should not crash just because one value was not what you expected.\n\n'
            'A try block lets you attempt something that might fail. If it does fail, Python jumps straight to a matching except block instead of crashing, and the rest of your program keeps running.'
        ),
        'starter_code': (
            'price_text = "twelve"\n'
            '\n'
            'try:\n'
            '    price = int(price_text)\n'
            '    print(f"Price: {price}")\n'
            'except ValueError:\n'
            '    print("That doesn\'t look like a valid number.")'
        ),
        'try_it': 'Change price_text to a real number in quotes, like "12", and run it again to see the try block succeed instead of the except block running.',
        'common_mistake': 'A bare except: with no error type catches every possible problem, including ones you did not expect, which can hide real bugs. Always name the specific error you are expecting, like except ValueError:.',
        'mini_challenge': 'Use try and except to divide 10 by divisor (set to 0). Catch ZeroDivisionError and print: Cannot divide by zero.',
        'challenge_starter_code': 'divisor = 0\n# Use try and except.\n# Try to divide 10 by divisor and print the result.\n# If a ZeroDivisionError happens, print: Cannot divide by zero.\n',
        'challenge_expected_output': 'Cannot divide by zero.',
        'expected_output': "That doesn't look like a valid number.",
        'practice_challenge_slug': 'safe-number-check',
        'quiz': [
            {
                'question': 'What happens when code inside a try block raises an error that matches an except line?',
                'options': [
                    'Python jumps to that except block and runs it instead of crashing.',
                    'The program stops immediately, the same as if there were no try block.',
                    'Python skips the rest of the file entirely.',
                ],
                'answer': 0,
                'explanation': 'The except block runs in place of a crash, and the program keeps going afterward.',
            },
            {
                'question': 'Why should except usually name a specific error type, like except ValueError, instead of a bare except:?',
                'options': [
                    'A bare except catches every kind of error, including ones you did not expect, which can hide real bugs.',
                    'Python requires a specific error type or the code will not run at all.',
                    'Naming the error type makes the code run faster.',
                ],
                'answer': 0,
                'explanation': 'Being specific means you only catch the problems you actually planned for.',
            },
            {
                'question': 'In the starter code, why does converting price_text to an int raise an error?',
                'options': [
                    '"twelve" is text, not digits, so int() cannot convert it to a number.',
                    'int() only works inside a function.',
                    'price_text was never assigned a value.',
                ],
                'answer': 0,
                'explanation': 'int() can only convert strings that actually look like whole numbers, such as "12".',
            },
        ],
    },
    {
        'slug': 'reading-and-writing-files',
        'module_slug': 'working-with-files',
        'title': 'Reading and Writing Files',
        'summary': 'Save data that sticks around after your program ends by reading and writing a simple text file.',
        'duration': '12 min',
        'goal': 'By the end, you will know how to write text to a file and read it back using a with block.',
        'explanation': (
            'Every variable you have used so far disappears the moment your program ends. Files are how you save information so it is still there the next time your program runs.\n\n'
            'The safest way to work with a file in Python is a with block. It opens the file, lets you read or write, and automatically closes it when you are done, even if something goes wrong partway through.'
        ),
        'starter_code': (
            'with open("notes.txt", "w") as file:\n'
            '    file.write("Practiced Python today.\\n")\n'
            '    file.write("Learned about files.\\n")\n'
            '\n'
            'with open("notes.txt", "r") as file:\n'
            '    contents = file.read()\n'
            '\n'
            'print(contents)'
        ),
        'try_it': 'Add a third file.write() line with another note, then run it again to see all three lines printed back.',
        'common_mistake': 'Forgetting the mode is a common mistake. Opening a file with "w" erases its previous contents before writing, so if you meant to add to a file instead of replacing it, use "a" for append instead.',
        'mini_challenge': 'Write two lines to goals.txt (My Python goals, then Practice daily), then open it again, read it, and print the contents.',
        'challenge_starter_code': '# Write two lines to goals.txt, each ending in a newline:\n#   My Python goals\n#   Practice daily\n# Then open goals.txt again, read it, and print the contents.\n',
        'challenge_expected_output': 'My Python goals\nPractice daily',
        'expected_output': 'Practiced Python today.\nLearned about files.\n',
        'practice_challenge_slug': 'write-and-read-a-file',
        'quiz': [
            {
                'question': 'What does a with block do when working with a file?',
                'options': [
                    'It automatically closes the file for you, even if an error happens.',
                    'It deletes the file after the program finishes.',
                    'It only works when reading a file, never when writing.',
                ],
                'answer': 0,
                'explanation': 'with handles closing the file safely, so you cannot forget to do it.',
            },
            {
                'question': "What happens if you open a file in \"w\" mode that already has content in it?",
                'options': [
                    'The existing content is erased before the new content is written.',
                    'The new content is automatically added to the end.',
                    'Python refuses to open the file.',
                ],
                'answer': 0,
                'explanation': '"w" mode always starts the file empty before writing.',
            },
            {
                'question': "Which mode would you use to add new lines to a file without erasing what's already there?",
                'options': [
                    '"a" for append.',
                    '"w" for write.',
                    '"r" for read.',
                ],
                'answer': 0,
                'explanation': 'Append mode adds new content after whatever is already in the file.',
            },
        ],
    },
    {
        'slug': 'importing-modules',
        'module_slug': 'modules-and-libraries',
        'title': 'Importing Modules',
        'summary': "Use Python's built-in toolbox — import a module like random instead of writing everything from scratch.",
        'duration': '10 min',
        'goal': 'By the end, you will know how to import a built-in module and use one of its functions in your own code.',
        'explanation': (
            'A module is a file full of ready-made Python code that someone else already wrote and tested. Python ships with a large standard library of built-in modules, so instead of writing your own logic for things like random numbers or dates, you can import a module and use it right away.\n\n'
            'To use a module, write import followed by its name at the top of your file. Then access anything inside it using module_name.thing_you_want, the same dot notation you have already used for strings and lists.'
        ),
        'starter_code': (
            'import random\n'
            '\n'
            'random.seed(7)\n'
            'lucky_number = random.randint(1, 100)\n'
            'print(f"Your lucky number is {lucky_number}.")'
        ),
        'try_it': 'Change the seed number and run it again to get a different lucky number.\nThen remove the random.seed(7) line entirely and run it a few times to see genuinely random results.',
        'common_mistake': 'Forgetting to write import random at the top is a common mistake; without it, Python has no idea what random refers to and raises a NameError. Another is calling randint() directly instead of random.randint(), since the function belongs to the module.',
        'mini_challenge': "Import random, set random.seed(1) so it is repeatable, then use random.choice() on ['walk', 'read', 'code'] and print the choice. Expected output: walk.",
        'challenge_starter_code': '# Import the random module.\n# Set random.seed(1) so the result is repeatable.\n# Use random.choice() on ["walk", "read", "code"] and print the choice.\n',
        'challenge_expected_output': 'walk',
        'expected_output': 'Your lucky number is 42.',
        'practice_challenge_slug': 'random-choice-picker',
        'quiz': [
            {
                'question': 'What is a module in Python?',
                'options': [
                    'A file of ready-made code you can import and reuse.',
                    'A special kind of variable that never changes.',
                    'A built-in error type.',
                ],
                'answer': 0,
                'explanation': 'Modules package up reusable code so you do not have to write everything yourself.',
            },
            {
                'question': 'Why does random.seed(7) make random.randint() produce the same result every time?',
                'options': [
                    'Seeding starts the random number generator from a fixed, repeatable point.',
                    'It disables randomness completely and always returns 7.',
                    'It only works the first time a program runs.',
                ],
                'answer': 0,
                'explanation': 'A fixed seed makes "random" results reproducible, which is useful for testing.',
            },
            {
                'question': 'What happens if you call randint() without writing random. in front of it?',
                'options': [
                    "Python raises a NameError because randint isn't defined on its own.",
                    'Python automatically assumes you mean the random module.',
                    'It works exactly the same as random.randint().',
                ],
                'answer': 0,
                'explanation': 'Functions that belong to a module must be accessed through that module.',
            },
        ],
    },
    {
        'slug': 'intro-to-classes-and-objects',
        'module_slug': 'intro-to-classes',
        'title': 'Your First Class',
        'summary': 'Bundle related data and behavior together by building your first simple class.',
        'duration': '14 min',
        'goal': 'By the end, you will know how to define a simple class with __init__, create an instance, and call a method on it.',
        'explanation': (
            'Every data type you have used so far, strings, lists, dictionaries, is built from a class. A class is a blueprint for creating objects: it defines what data an object holds and what it can do.\n\n'
            'Once you define a class, you can create as many independent objects from it as you want, called instances. Each instance has its own copy of the data, even though they all share the same blueprint.'
        ),
        'starter_code': (
            'class Student:\n'
            '    def __init__(self, name, favorite_topic):\n'
            '        self.name = name\n'
            '        self.favorite_topic = favorite_topic\n'
            '\n'
            '    def introduce(self):\n'
            '        print(f"Hi, I\'m {self.name} and I\'m learning about {self.favorite_topic}.")\n'
            '\n'
            'learner = Student("Michael", "functions")\n'
            'learner.introduce()'
        ),
        'try_it': 'Create a second Student with your own name and favorite topic, then call introduce() on it too.\nNotice the two students do not affect each other.',
        'common_mistake': 'Forgetting self as the first parameter in __init__ and every method is one of the most common class mistakes; without it, Python has no way to attach data to that specific instance. Another is forgetting to actually create an instance, like learner = Student(...), and trying to call introduce() on the class itself.',
        'mini_challenge': 'Complete the Student class so it stores name and streak_days, and add a method show_streak() that prints: Sam has a 5 day streak.',
        'challenge_starter_code': '# Complete the Student class so show_streak() prints: Sam has a 5 day streak.\nclass Student:\n    def __init__(self, name, streak_days):\n        # store name and streak_days on self\n        pass\n\n    def show_streak(self):\n        # print the streak sentence using an f-string\n        pass\n\nlearner = Student("Sam", 5)\nlearner.show_streak()\n',
        'challenge_expected_output': 'Sam has a 5 day streak.',
        'expected_output': "Hi, I'm Michael and I'm learning about functions.",
        'practice_challenge_slug': 'build-a-pet-class',
        'quiz': [
            {
                'question': 'What does __init__ do in a class?',
                'options': [
                    'It runs automatically when a new instance is created and sets up its starting attributes.',
                    'It deletes an instance when the program ends.',
                    'It only runs if you call it by name after creating the object.',
                ],
                'answer': 0,
                'explanation': '__init__ is Python\'s way of setting up a new object\'s starting data.',
            },
            {
                'question': 'What does self refer to inside a method?',
                'options': [
                    'The specific instance the method is being called on.',
                    'The class itself, shared by every instance.',
                    'A built-in Python keyword unrelated to the object.',
                ],
                'answer': 0,
                'explanation': 'self lets a method read and change data that belongs to one particular instance.',
            },
            {
                'question': "If you create two Student instances with different names, why doesn't changing one affect the other?",
                'options': [
                    'Each instance stores its own independent copy of the attributes.',
                    'Python automatically links all instances of the same class together.',
                    'Only the first instance created actually stores real data.',
                ],
                'answer': 0,
                'explanation': 'Instances are independent, even though they share the same class blueprint.',
            },
        ],
    },
]

# Draft lessons awaiting review. These fill modules that currently have no
# lessons at all (input-and-output, debugging-basics, mini-projects,
# next-steps). They are seeded into the database as unpublished via
# `manage.py bootstrap_learning_content` and only appear on the live site
# once a reviewer flips is_published to True in Django admin.
DRAFT_LESSONS = [
    {
        'slug': 'getting-user-input',
        'module_slug': 'input-and-output',
        'title': 'Getting Input from Users',
        'summary': 'Use input() to collect what someone types and turn it into a personalized response.',
        'duration': '10 min',
        'goal': 'By the end, you will know how to use input() to collect text from a user and combine it with an f-string for a friendly response.',
        'explanation': 'input() pauses your program and waits for someone to type something, then hands that text back to you as a string. Pair it with an f-string and a script that only ever prints the same thing can start responding to the person actually using it. Since this editor cannot show a real typing prompt, use the Sample input box below the code editor to supply the value input() will receive when you press Run.',
        'starter_code': 'name = input("What is your name? ")\nprint(f"Nice to meet you, {name}!")',
        'try_it': 'Type a name into the Sample input box below the editor and press Run. Then add a second input() that asks for a favorite hobby (add a second line to Sample input too) and include it in the printed message.',
        'common_mistake': 'input() always returns a string, even when someone types a number. Trying to do math on it directly raises a TypeError. Convert it first with int() or float().',
        'mini_challenge': 'Ask for someone\'s age with input(), convert it to an integer, and print how old they will be in 10 years.',
        'expected_output': 'What is your name? Michael\nNice to meet you, Michael!',
        'practice_challenge_slug': '',
        'quiz': [
            {
                'question': 'What type of value does input() always return?',
                'options': [
                    'A string, even if the text looks like a number.',
                    'Whatever type matches what the user typed.',
                    'An integer.',
                ],
                'answer': 0,
                'explanation': 'input() reads text from the keyboard and always hands it back as a string, no matter what was typed.',
            },
            {
                'question': 'Why does this code raise an error?\nage = input("Age: ")\nnext_year = age + 1',
                'options': [
                    'You cannot add an integer to a string without converting first.',
                    'input() only works with words.',
                    'print() was left out.',
                ],
                'answer': 0,
                'explanation': 'age is a string, so Python cannot add the integer 1 to it directly. Wrap it in int(age) first.',
            },
            {
                'question': 'What does an f-string let you do?',
                'options': [
                    'Insert a variable\'s value directly inside a string using curly braces.',
                    'Ask the user for input.',
                    'Convert a string to a number.',
                ],
                'answer': 0,
                'explanation': 'An f-string, written as f"...{variable}...", drops a variable\'s value straight into the text.',
            },
        ],
    },
    {
        'slug': 'reading-errors-and-debugging',
        'module_slug': 'debugging-basics',
        'title': 'Reading Error Messages and Debugging',
        'summary': 'Read a traceback calmly, find the real problem line, and use print() to see what your code is actually doing.',
        'duration': '10 min',
        'goal': 'By the end, you will know how to read a Python traceback and use print statements to track down what a program is doing before it breaks.',
        'explanation': 'A traceback looks intimidating, but it is really just Python telling you exactly where it got stuck. Read it from the bottom up: the last line names the error type, and the line above it points to the exact line of your code that caused it. When the cause is not obvious, add a print() before the problem line to see what a variable actually holds at that moment.',
        'starter_code': 'price = "12"\ntax = 0.08\ntotal = price + tax\nprint(f"Total: {total}")',
        'try_it': 'Run the code, read the error at the bottom, then fix it by converting price to a float before adding tax.',
        'common_mistake': 'It is tempting to only read the last line of a traceback. The last line names the error, but the line just above it points to exactly where to look in your own code.',
        'mini_challenge': 'Add a print(type(price)) line right before the broken line so you can see the exact type causing the problem, then fix the bug.',
        'expected_output': 'TypeError: can only concatenate str (not "float") to str\n\nThis error is expected: price is still text ("12"), so Python cannot add it to the tax number yet. Fix it by converting price to a float (float(price) + tax) and you will see: Total: 12.08',
        'practice_challenge_slug': '',
        'quiz': [
            {
                'question': 'When reading a Python traceback, where should you look first?',
                'options': [
                    'The last line, which names the type of error.',
                    'The very first line of the file.',
                    'The middle of the traceback.',
                ],
                'answer': 0,
                'explanation': 'The last line of a traceback names the error type and usually explains what went wrong in plain language.',
            },
            {
                'question': 'What is a quick way to check what value a variable actually holds while debugging?',
                'options': [
                    'Add a print() statement right before the line that fails.',
                    'Delete the variable and try again.',
                    'Rename the variable.',
                ],
                'answer': 0,
                'explanation': 'Printing a variable right before the problem line shows you exactly what Python is working with at that moment.',
            },
            {
                'question': 'What does a TypeError usually mean?',
                'options': [
                    'An operation was used on values of a type that does not support it, like adding a string and a number.',
                    'The internet connection dropped.',
                    'A file could not be found.',
                ],
                'answer': 0,
                'explanation': 'TypeError shows up when you try to combine or use values in a way their types do not support, such as price + tax when price is still a string.',
            },
        ],
    },
    {
        'slug': 'building-a-mini-program',
        'module_slug': 'mini-projects',
        'title': 'From Concepts to a Mini Program',
        'summary': 'Combine input, conditionals, and f-strings into one small, complete program.',
        'duration': '12 min',
        'goal': 'By the end, you will know how to plan a tiny program in plain English first, then build it a few lines at a time using concepts you already know.',
        'explanation': 'Every mini project is just a handful of lessons stacked together. The trick is not learning something new, it is deciding, in plain English, what the program should do step by step before writing any code. Once you have a short list of steps, each one usually maps to a line or two of Python you already know: input() to collect something, a variable to store it, an if statement to react to it, and an f-string to explain the result. This lesson uses two input() calls, so add two lines to the Sample input box below the editor before pressing Run: one for the budget, one for the amount spent.',
        'starter_code': 'budget = float(input("What is your budget? "))\nspent = float(input("How much have you spent? "))\nremaining = budget - spent\n\nif remaining < 0:\n    print(f"You are over budget by ${-remaining:.2f}.")\nelse:\n    print(f"You have ${remaining:.2f} left.")',
        'try_it': 'Add a third message for when remaining is exactly 0, letting the user know they spent their budget exactly.',
        'common_mistake': 'Trying to write the whole program in one go often stalls beginners. Write the plain-English steps as comments first, then fill in one line of code per comment.',
        'mini_challenge': 'Extend the program to also print a warning message if remaining is less than 10% of the original budget, even if it is not negative yet.',
        'expected_output': 'What is your budget? 100\nHow much have you spent? 40\nYou have $60.00 left.',
        'practice_challenge_slug': '',
        'quiz': [
            {
                'question': 'What is the first step when planning a mini program?',
                'options': [
                    'Write out the steps in plain English before writing any code.',
                    'Start typing code immediately and fix errors as they come up.',
                    'Pick the fanciest feature you know and use it.',
                ],
                'answer': 0,
                'explanation': 'Planning the steps in plain English first makes it much easier to see which small piece of Python each step needs.',
            },
            {
                'question': 'In the starter code, why is float() used around each input() call?',
                'options': [
                    'input() always returns a string, and the program needs to do math with the values.',
                    'float() prints the value to the screen.',
                    'It is required syntax for every input() call.',
                ],
                'answer': 0,
                'explanation': 'Since input() always returns a string, float() converts the typed text into a number so it can be used in subtraction.',
            },
            {
                'question': 'Why break a mini project into small steps instead of writing it all at once?',
                'options': [
                    'Each small step is easier to test and debug on its own.',
                    'Python requires programs to be written in small steps.',
                    'It makes the program run faster.',
                ],
                'answer': 0,
                'explanation': 'Testing one small piece at a time makes it much easier to catch a mistake before it gets buried under more code.',
            },
        ],
    },
    {
        'slug': 'installing-python-and-next-steps',
        'module_slug': 'next-steps',
        'title': 'Installing Python and What to Do Next',
        'summary': 'Set up Python and a code editor on your own computer, then pick a clear next step to keep building.',
        'duration': '10 min',
        'goal': 'By the end, you will know how to install Python locally, open your first file in a code editor, and choose one concrete next step to keep learning.',
        'explanation': 'Everything so far has run in the browser so you could focus on learning, not setup. Installing Python locally is a short one-time step that unlocks bigger projects: install Python from python.org, install a free code editor like VS Code, then create a file ending in .py and run it from a terminal with python filename.py. From there, the fastest way to keep momentum is picking one small, concrete goal rather than trying to learn everything at once.',
        'starter_code': '# This is what a local Python file looks like.\n# Save this as hello.py and run it with: python hello.py\n\nprint("Hello from my own computer!")',
        'try_it': 'Imagine you just installed Python locally. Change this comment to describe the exact command you would type to run a file named practice.py.',
        'common_mistake': 'Beginners often try to learn a code editor, git, and a new project all at the same time. Set up one piece, get it working, then move to the next so each step feels manageable.',
        'mini_challenge': 'Write down one project idea from the Projects page and one new topic you want to learn next, in your own words.',
        'expected_output': 'Hello from my own computer!',
        'practice_challenge_slug': '',
        'quiz': [
            {
                'question': 'What is the first step to running Python outside the browser?',
                'options': [
                    'Install Python from python.org.',
                    'Buy a new computer.',
                    'Learn a new programming language first.',
                ],
                'answer': 0,
                'explanation': 'Installing Python from the official python.org site is the standard first step to running Python locally.',
            },
            {
                'question': 'What command runs a local Python file named hello.py from a terminal?',
                'options': [
                    'python hello.py',
                    'run hello.py',
                    'open hello.py',
                ],
                'answer': 0,
                'explanation': 'Typing python followed by the filename tells your computer to run that file with Python.',
            },
            {
                'question': 'Why is it better to set up one new tool at a time instead of everything at once?',
                'options': [
                    'Each piece is easier to get working and troubleshoot on its own.',
                    'Python requires tools to be installed in a specific order.',
                    'It is required by python.org.',
                ],
                'answer': 0,
                'explanation': 'Setting up one tool at a time keeps troubleshooting simple, since you know exactly what changed if something breaks.',
            },
        ],
    },
]

CHALLENGES = [
    {
        'slug': 'warm-up-greeting',
        'title': 'Warm-up Greeting',
        'difficulty': 'Beginner',
        'prompt': 'Write two print() lines: one greeting and one line that shares your learning goal.',
        'hint': 'You can copy the lesson example and change the words inside the quotes.',
        'starter_code': 'print("Hello, Python learner!")\nprint("My goal is to finish my first lesson.")',
        'expected_output': 'Hello, Python learner!\nMy goal is to finish my first lesson.',
        'success_checks': [
            'Your code runs without a syntax error.',
            'You printed two separate lines.',
            'One line includes a greeting and the other includes a learning goal.',
        ],
        'reflection_prompt': 'What changed when you rewrote the text to sound more like you?',
    },
    {
        'slug': 'simple-scoreboard',
        'title': 'Simple Scoreboard',
        'difficulty': 'Beginner',
        'prompt': 'Create output for a team name and score using separate print() lines.',
        'hint': 'Try values like "Tigers" and 7 to keep it playful and practical.',
        'starter_code': 'team_name = "Tigers"\nteam_score = 7\n\nprint(team_name)\nprint(team_score)',
        'expected_output': 'Tigers\n7',
        'success_checks': [
            'You created both a team name and a score value.',
            'Your output prints on separate lines.',
            'You changed at least one of the starter values.',
        ],
        'reflection_prompt': 'If you wanted to turn this into a real scoreboard later, what extra value would you store next?',
    },
    {
        'slug': 'mood-check',
        'title': 'Mood Check',
        'difficulty': 'Beginner',
        'prompt': 'Display a short three-line check-in: your name, your mood, and a goal for the week.',
        'hint': 'Each piece of information can have its own print() line.',
        'starter_code': 'name = "Michael"\nmood = "curious"\ngoal = "practice Python for 20 minutes"\n\nprint(name)\nprint(mood)\nprint(goal)',
        'expected_output': 'Michael\ncurious\npractice Python for 20 minutes',
        'success_checks': [
            'You stored three pieces of information in variables.',
            'Each variable is printed on its own line.',
            'The values reflect your own check-in rather than the starter text.',
        ],
        'reflection_prompt': 'Which of these three variables felt most natural to change first, and why?',
    },
    {
        'slug': 'data-type-mix-up',
        'title': 'Data Type Mix-Up',
        'difficulty': 'Beginner',
        'prompt': 'Create one int, one float, and one string, then print them together in one f-string summary.',
        'hint': 'Try values like 7, 1.5, and "Python".',
        'starter_code': 'completed_lessons = 7\nstudy_hours = 1.5\nfavorite_language = "Python"\n\nprint(f"Lessons: {completed_lessons}, Hours: {study_hours}, Language: {favorite_language}")',
        'expected_output': 'Lessons: 7, Hours: 1.5, Language: Python',
        'success_checks': [
            'Your code includes an int, a float, and a string.',
            'You used an f-string to print the summary.',
            'The output clearly shows all three values.',
        ],
        'reflection_prompt': 'Which of these data types still feels the least familiar, and how can you tell it apart from the others?',
    },
    {
        'slug': 'boolean-checkpoint',
        'title': 'Boolean Checkpoint',
        'difficulty': 'Beginner',
        'prompt': 'Create a boolean called practiced_today and use a simple if statement to print a message when it is True.',
        'hint': 'Try practiced_today = True, then use if practiced_today: to print your message.',
        'starter_code': 'practiced_today = True\n\nif practiced_today:\n    print("Nice! You showed up today.")',
        'expected_output': 'Nice! You showed up today.',
        'success_checks': [
            'You created a boolean variable.',
            'You used a simple if statement to check it.',
            'Your message prints when the boolean is True.',
        ],
        'reflection_prompt': 'What would you add so a different message prints when the boolean is False?',
    },
    {
        'slug': 'conditional-coach',
        'title': 'Conditional Coach',
        'difficulty': 'Building Confidence',
        'prompt': 'Create a score variable and use if, elif, and else to print different feedback messages.',
        'hint': 'Try one branch for high scores, one for medium scores, and one for lower scores.',
        'starter_code': 'score = 85\n\nif score >= 90:\n    print("Amazing work!")\nelif score >= 70:\n    print("Nice progress!")\nelse:\n    print("Keep practicing!")',
        'expected_output': 'Nice progress!',
        'success_checks': [
            'You used if, elif, and else together.',
            'Each branch prints a different message.',
            'Changing the score changes which message appears.',
        ],
        'reflection_prompt': 'What score would you test next to prove a different branch is working?',
    },
    {
        'slug': 'list-and-dictionary-snapshot',
        'title': 'List and Dictionary Snapshot',
        'difficulty': 'Building Confidence',
        'prompt': 'Make a list of three topics and a dictionary with your name and current goal, then print one value from each.',
        'hint': 'Use square brackets for lists and curly braces with keys for dictionaries.',
        'starter_code': 'topics = ["variables", "loops", "functions"]\nstudent_profile = {"name": "Michael", "goal": "Finish beginner Python"}\n\nprint(topics[0])\nprint(student_profile["goal"])',
        'expected_output': 'variables\nFinish beginner Python',
        'success_checks': [
            'You created both a list and a dictionary.',
            'You printed one item from the list.',
            'You printed one value from the dictionary using its key.',
        ],
        'reflection_prompt': 'If you added one more key to the dictionary, what would be most useful to store there?',
    },
    {
        'slug': 'loop-through-a-list',
        'title': 'Loop Through a List',
        'difficulty': 'Building Confidence',
        'prompt': 'Create a list of three practice topics and use a for loop to print each one.',
        'hint': 'A list uses square brackets, like ["topic one", "topic two"].',
        'starter_code': 'topics = ["variables", "strings", "loops"]\n\nfor topic in topics:\n    print(topic)',
        'expected_output': 'variables\nstrings\nloops',
        'success_checks': [
            'You created a list with three values.',
            'You used a for loop to print each value.',
            'The printed output shows one topic per line.',
        ],
        'reflection_prompt': 'How would the output change if you added one more topic to the list?',
    },
    {
        'slug': 'tuple-to-loop',
        'title': 'Tuple to Loop',
        'difficulty': 'Building Confidence',
        'prompt': 'Make a tuple of three beginner Python topics and use a for loop to print each one.',
        'hint': 'A tuple uses parentheses, like ("ints", "strings", "loops").',
        'starter_code': 'topics = ("ints", "strings", "loops")\n\nfor topic in topics:\n    print(topic)',
        'expected_output': 'ints\nstrings\nloops',
        'success_checks': [
            'You created a tuple with three values.',
            'You used a for loop to print each value.',
            'The printed output shows one topic per line.',
        ],
        'reflection_prompt': 'How would the output change if you added one more topic to the tuple?',
    },
    {
        'slug': 'function-practice',
        'title': 'Function Practice',
        'difficulty': 'Stretch',
        'prompt': 'Write a function that accepts a name and prints a welcome message with an f-string.',
        'hint': 'Start with def welcome_student(name): and return or print one sentence.',
        'starter_code': 'def welcome_student(name):\n    print(f"Welcome, {name}!")\n\nwelcome_student("Michael")',
        'expected_output': 'Welcome, Michael!',
        'success_checks': [
            'You defined a function with a parameter.',
            'You used an f-string inside the function.',
            'You called the function so output actually appeared.',
        ],
        'reflection_prompt': 'What second argument could you add later to make this welcome message more flexible?',
    },
    {
        'slug': 'safe-number-check',
        'title': 'Safe Number Check',
        'difficulty': 'Stretch',
        'prompt': 'Try to convert a text value to an int inside a try block, and print a friendly message in except ValueError if it fails.',
        'hint': 'Use try: ... except ValueError: ... around int(some_text).',
        'starter_code': 'age_text = "twenty"\n\ntry:\n    age = int(age_text)\n    print(f"Age: {age}")\nexcept ValueError:\n    print("That doesn\'t look like a valid age.")',
        'expected_output': "That doesn't look like a valid age.",
        'success_checks': [
            'You used a try block around a conversion that can fail.',
            'You used except ValueError to catch the problem.',
            'Your except block prints a friendly message instead of crashing.',
        ],
        'reflection_prompt': 'What would happen if age_text held a valid number instead — which block would run?',
    },
    {
        'slug': 'write-and-read-a-file',
        'title': 'Write and Read a File',
        'difficulty': 'Stretch',
        'prompt': 'Write two lines to a file called log.txt, then open it again and print its contents.',
        'hint': 'Use with open("log.txt", "w") as file: to write, then a separate with open("log.txt", "r") as file: to read.',
        'starter_code': 'with open("log.txt", "w") as file:\n    file.write("Started learning Python.\\n")\n    file.write("Finished the files lesson.\\n")\n\nwith open("log.txt", "r") as file:\n    print(file.read())',
        'expected_output': 'Started learning Python.\nFinished the files lesson.\n',
        'success_checks': [
            'You wrote two lines to a file using file.write().',
            'You reopened the file in read mode.',
            "You printed the file's contents.",
        ],
        'reflection_prompt': 'What would happen if you ran the write block a second time without changing anything?',
    },
    {
        'slug': 'random-choice-picker',
        'title': 'Random Choice Picker',
        'difficulty': 'Stretch',
        'prompt': 'Import the random module and use random.choice() to print one item picked randomly from a list of three snacks.',
        'hint': 'Use random.choice(your_list) after import random.',
        'starter_code': 'import random\n\nrandom.seed(3)\nsnacks = ["pretzels", "grapes", "trail mix"]\nprint(random.choice(snacks))',
        'expected_output': 'pretzels',
        'success_checks': [
            'You imported the random module.',
            'You used random.choice() on a list.',
            'The output shows one randomly chosen item.',
        ],
        'reflection_prompt': 'What would you need to change to pick two snacks instead of one?',
    },
    {
        'slug': 'build-a-pet-class',
        'title': 'Build a Pet Class',
        'difficulty': 'Advanced',
        'prompt': 'Create a Pet class with a name and sound, and a method that prints a greeting using both.',
        'hint': 'Give __init__ two parameters besides self, and store them with self.name = name and self.sound = sound.',
        'starter_code': 'class Pet:\n    def __init__(self, name, sound):\n        self.name = name\n        self.sound = sound\n\n    def greet(self):\n        print(f"{self.name} says {self.sound}!")\n\nbuddy = Pet("Buddy", "Woof")\nbuddy.greet()',
        'expected_output': 'Buddy says Woof!',
        'success_checks': [
            'You defined a class with __init__.',
            'You created an instance of the class.',
            "You called a method that used the instance's own data.",
        ],
        'reflection_prompt': 'What would you add to Pet to track how many times it has been fed?',
    },
]

PROJECTS = [
    {'title': 'Tip Calculator', 'description': 'Use input, math, and formatted output to total a restaurant bill.'},
    {'title': 'Quiz Game', 'description': 'Ask a few questions, keep score, and celebrate the final result.'},
    {'title': 'Budget Tracker', 'description': 'Store categories in variables or lists and summarize spending.'},
]

TIPS = [
    {
        'title': 'Read the line above the error',
        'description': 'A missing quote or parenthesis often breaks the next line, so do not trust the last line alone.',
    },
    {
        'title': 'Change one thing at a time',
        'description': 'When you are learning, smaller edits make it easier to see what caused the output to change.',
    },
    {
        'title': 'Say the code out loud',
        'description': 'Reading a line like print("Hello") as a sentence can make Python feel less abstract.',
    },
]

RESOURCES = []

COMMUNITY_ITEMS = [
    {
        'title': 'Monday Teach',
        'description': 'Share a quick concept on social, then link back to the full lesson for deeper practice.',
    },
    {
        'title': 'Wednesday Challenge',
        'description': 'Post a prompt, invite comments with solutions, and feature the browser editor on-site.',
    },
    {
        'title': 'Friday Fix',
        'description': 'Break down a common mistake in plain English and celebrate learner progress.',
    },
]

# The full "Python for Absolute Beginners" premium course, unlocked with a
# one-time purchase after finishing the free lesson path. Sections with a
# 'lectures' key have their full text ported in; sections with only a
# 'topics' key show the curriculum outline while their content is still
# being ported. Both render on the course page so purchasers can see the
# complete scope even before every lecture is filled in.
PREMIUM_COURSE_SECTIONS = [
    {
        'title': 'Introduction',
        'lectures': [
            {
                'title': 'Welcome to the Course',
                'body': (
                    'Welcome to "Python for Absolute Beginners." I\'m really glad you\'re here.\n\n'
                    "Whether you've always been curious about programming but never knew where to start, or you've tried to learn before and found it overwhelming, this course was built with you in mind. We're starting from zero. No experience required. No assumptions made.\n\n"
                    "My name is Mike and I'll be your guide throughout this course. By the end of it you'll have a genuine foundation in one of the most popular and versatile programming languages in the world, and you'll have built real, working programs along the way.\n\n"
                    "And I mean real. Not fill-in-the-blank exercises or isolated snippets that don't go anywhere. Actual programs: a Mad Libs generator, a number guessing game, a shopping list app, a contact book, a tip calculator, a to-do list that saves your data, and more. Every concept we cover gets applied to something you can run, play with, and be proud of.\n\n"
                    "Here's what you'll learn:\n"
                    '- What Python is and how it works\n'
                    '- How to store and work with data using variables and data types\n'
                    '- How to make programs that respond to user input\n'
                    '- How to work with lists, dictionaries, and other data structures\n'
                    '- How to write clean, reusable code with functions\n'
                    "- How to handle errors gracefully so your programs don't crash\n"
                    '- How to read and write files so your data persists\n'
                    '- How to extend Python with built-in and external modules\n'
                    '- How to think in objects with an introduction to classes\n\n'
                    "Take your time with each section. Rewatch lectures if something doesn't click the first time. Try the mini projects before looking at the solutions — even if your attempt isn't perfect, the struggle is where the learning actually happens.\n\n"
                    "Every professional developer was once a beginner. Keep that in mind, and let's get started."
                ),
            },
        ],
    },
    {
        'title': 'Section 1: Getting Started',
        'goal': 'Get set up and write your first Python code.',
        'lectures': [
            {
                'title': 'What is Python and Why Learn It?',
                'body': (
                    "Before we write a single line of code, let's take a moment to talk about what Python actually is and why it's worth your time.\n\n"
                    "Python is a high-level, general-purpose programming language, which is a fancy way of saying it's a tool that lets you give instructions to a computer in a way that's close to plain English. It was created in the late 1980s by a developer named Guido van Rossum, and it was designed from the very beginning with one goal in mind: to be easy to read and easy to write.\n\n"
                    "That philosophy has made Python one of the most popular programming languages in the world. It's used everywhere, from building websites and web applications, to analyzing data, automating repetitive tasks, developing artificial intelligence, and even controlling hardware. Companies like Google, Netflix, Instagram, and NASA all use Python in their day-to-day work.\n\n"
                    "So why are we learning it?\n\n"
                    "It's beginner friendly — the syntax, meaning the rules for how you write Python code, is clean and readable. It looks more like written English than a foreign language, which means you spend less time deciphering strange symbols and more time actually learning how to think like a programmer.\n\n"
                    "It's versatile — once you know Python, you're not locked into one type of project. The skills you build here will apply whether you want to build websites, work with data, or automate things in your daily life.\n\n"
                    "It's a gateway — every concept we cover lays the groundwork for real-world programming. Python is also the foundation for Django, a web framework used to build full web applications.\n\n"
                    "By the end of this course, you won't just know Python syntax. You'll know how to think through a problem, break it into steps, and write code that actually does something useful. That's what programming really is."
                ),
            },
            {
                'title': 'Installing Python & VS Code',
                'body': (
                    "Before we can write any code, we need two things installed on your computer: Python itself, and VS Code, the code editor we'll be writing in.\n\n"
                    'Installing Python: head to python.org/downloads and download the installer for your operating system.\n\n'
                    'Windows users — at the bottom of the installer, check the box that says "Add Python to PATH" before you click Install. If you miss this, Python won\'t be recognized in the terminal.\n\n'
                    'Mac users — the installer is straightforward. Just follow the prompts.\n\n'
                    'Once installed, verify it worked: open a terminal and type python --version (or python3 --version on Mac/Linux). You should see a version number printed back.\n\n'
                    'Installing VS Code: head to code.visualstudio.com and download it for your operating system. Once it\'s open, click the Extensions icon in the left sidebar, search for "Python," and install the one published by Microsoft. This gives you syntax highlighting, error detection, and code suggestions.'
                ),
            },
            {
                'title': 'The Python Terminal vs Writing Scripts',
                'body': (
                    "Now that everything is installed, let's talk about the two main ways you can run Python code.\n\n"
                    "The Python terminal, also called the interactive interpreter or REPL (Read, Evaluate, Print, Loop), is a live environment where you type one line of Python at a time and see the result immediately. Open a terminal and type python, then try typing 2 + 2 and pressing Enter — Python responds with 4 instantly.\n\n"
                    "The terminal is great for testing quick ideas, but it has one big limitation: nothing you type there is saved. The moment you close it, it's gone.\n\n"
                    "That's where scripts come in. A Python script is a text file with a .py extension that contains Python code. Instead of typing one line at a time, you write your entire program, save it, and run it all at once. This is how real Python programs are written, and how we'll work throughout this course."
                ),
            },
            {
                'title': 'Your First Program',
                'body': (
                    "This is one of those moments every programmer remembers. Let's write your first line of Python code.\n\n"
                    'Create a file called hello.py and type:\n\n'
                    'print("Hello, World!")\n\n'
                    "That's it. That's your first program.\n\n"
                    "print() is a built-in Python function — a command that tells Python to do something. Specifically, it tells Python to display whatever is inside the parentheses on the screen. \"Hello, World!\" is a string, a piece of text wrapped in quotation marks. Put them together and Python reads it as: \"take this text and display it.\"\n\n"
                    'Try changing the text inside the quotes to anything you like. print() doesn\'t care what\'s inside — it just displays it.'
                ),
            },
            {
                'title': 'How to Run a Python File',
                'body': (
                    "Now that we have code written, let's run it. There are two ways to do this in VS Code.\n\n"
                    "Option 1 — the Run button: in the top right corner of VS Code you'll see a Play button. Click it and VS Code runs your script automatically, showing the output in a terminal panel at the bottom. This is the quickest way and the one you'll use most often.\n\n"
                    "Option 2 — the terminal: open a terminal in VS Code (Terminal → New Terminal) and type python hello.py (or python3 hello.py on Mac/Linux), then press Enter.\n\n"
                    'Both options do exactly the same thing: they tell Python to read your file and execute the code inside it.'
                ),
            },
            {
                'title': 'Comments and Code Readability',
                'body': (
                    "As your programs grow, it becomes important to write code that's easy to understand — not just for other people, but for yourself when you come back to it later. One of the most important tools for this is the comment.\n\n"
                    "A comment is a line in your code that Python completely ignores. It's there purely for the human reading the code. In Python, you write a comment by starting a line with a # symbol:\n\n"
                    '# This is a comment\n'
                    'print("Hello, World!")  # This prints a greeting to the screen\n\n'
                    "Python skips every line that starts with # and everything after a # on the same line. It has no effect on how your program runs.\n\n"
                    "A few good habits: write comments for anything that isn't immediately obvious, keep them short, update them when you update your code (an outdated comment is worse than no comment at all), and don't over-comment — a comment like # prints hello above print(\"hello\") adds nothing.\n\n"
                    "Good readability is a habit worth building from day one. Code is read far more often than it's written."
                ),
            },
            {
                'title': 'Mini Project: Introduce Yourself',
                'body': (
                    "You've learned how to write and run a Python script, use print(), and add comments. Now let's put it all together.\n\n"
                    'The challenge: write a script that introduces yourself, printing your name, age, city, why you\'re learning Python, and a fun fact. Use comments to label each section. Give it a try before looking at the solution below.\n\n'
                    'Solution:\n\n'
                    '# My Introduction\n'
                    '# Name\n'
                    'print("Hi! My name is Mike.")\n'
                    '# Age\n'
                    'print("I am 44 years old.")\n'
                    '# Location\n'
                    'print("I live in Boston, Massachusetts.")\n'
                    "# Why I'm learning Python\n"
                    'print("I\'m learning Python because I want to build my own web applications.")\n'
                    '# Fun fact\n'
                    'print("Fun fact: I play baseball in an over 40 league.")\n\n'
                    "A few things to note: print() is called once per line of output, and each call starts a new line automatically. Comments label each section clearly without affecting the output. And the text reads like a natural introduction rather than raw data — that's intentional. Even at this early stage, thinking about how your output looks to the reader is good programming practice."
                ),
            },
        ],
    },
    {
        'title': 'Section 2: Variables & Data Types',
        'goal': 'Understand how Python stores and works with data.',
        'lectures': [
            {
                'title': 'What is a Variable?',
                'body': (
                    "In the last section we wrote our first Python script and used print() to display text on the screen, but every time we ran the program, it printed the exact same thing. Real programs need to work with data that changes — names, numbers, scores, prices — and to do that, we need variables.\n\n"
                    "A variable is a named container that stores a value. Think of it like a labeled box. You put something in the box, give the box a name, and then whenever you need that value you just refer to the box by its name.\n\n"
                    "In Python, creating a variable looks like this:\n\n"
                    'name = "Mike"\n'
                    'age = 44\n'
                    'location = "Boston"\n\n'
                    'The first line creates a box called name and puts the value "Mike" inside it. The second creates a box called age and puts 44 inside it. The third creates a box called location and stores "Boston" inside it. That = sign is called the assignment operator. It doesn\'t mean "equals" the way it does in math — it means "take the value on the right and store it in the variable on the left."\n\n'
                    'Once a variable is created, you can use it anywhere in your program, and you can update its value at any time simply by assigning it again:\n\n'
                    'age = 44\n'
                    'print(age)\n'
                    'age = 45\n'
                    'print(age)\n\n'
                    'Output:\n'
                    '44\n'
                    '45\n\n'
                    "The old value is replaced by the new one. The variable always holds whatever was most recently assigned to it.\n\n"
                    "A few naming rules: variable names can contain letters, numbers, and underscores, but can't start with a number. They're case sensitive — name, Name, and NAME are three different variables. They can't be Python keywords like print, if, for, or while. By convention, Python variable names use snake_case: all lowercase with underscores between words, like first_name or total_price. Good variable names are descriptive — age is better than a, total_price is better than tp. Your future self will thank you."
                ),
            },
            {
                'title': 'Strings',
                'body': (
                    'The first data type we\'re going to look at is the string. A string is any sequence of characters — letters, numbers, symbols, spaces — wrapped in quotation marks. We already used strings in the last section when we wrote print("Hello, World!").\n\n'
                    'first_name = "Mike"\n'
                    'city = "Boston"\n\n'
                    "You can use either single quotes or double quotes — Python treats them the same way. Just be consistent within a single string.\n\n"
                    'You can combine strings together using the + operator, called concatenation:\n\n'
                    'first_name = "Mike"\n'
                    'last_name = "Smith"\n'
                    'full_name = first_name + " " + last_name\n'
                    'print(full_name)\n\n'
                    'Output:\n'
                    'Mike Smith\n\n'
                    'Notice we added " ", a string containing just a space, between the two names. Without it, the output would be MikeSmith. You can also repeat a string using the * operator: print("Ha" * 3) prints HaHaHa.\n\n'
                    "Python also comes with built-in tools for working with strings called methods. A method is called by placing a dot after the variable name followed by the method name and parentheses:\n\n"
                    'name = "mike Smith"\n'
                    'print(name.upper())       # MIKE SMITH\n'
                    'print(name.lower())       # mike smith\n'
                    'print(name.title())       # Mike Smith\n'
                    'print(name.replace("mike", "bill"))  # bill Smith\n'
                    'print(len(name))          # 10 — this is a function, not a method\n\n'
                    ".upper() converts to uppercase, .lower() converts to lowercase, .title() capitalizes the first letter of each word, and .replace() swaps one substring for another. len() returns the number of characters in the string — it's technically a built-in function rather than a method, but you'll use it constantly with strings."
                ),
            },
            {
                'title': 'Integers & Floats',
                'body': (
                    "Python has two main numeric data types: integers and floats.\n\n"
                    "An integer is a whole number — no decimal point, positive, negative, or zero:\n\n"
                    'age = 44\n'
                    'year = 2026\n'
                    'temperature = -10\n\n'
                    'A float is a number with a decimal point:\n\n'
                    'price = 9.99\n'
                    'height = 5.11\n\n'
                    'Python supports all the standard math operations:\n\n'
                    'a = 10\n'
                    'b = 3\n'
                    'print(a + b)   # 13  — addition\n'
                    'print(a - b)   # 7   — subtraction\n'
                    'print(a * b)   # 30  — multiplication\n'
                    'print(a / b)   # 3.333...  — division (always returns a float)\n'
                    'print(a // b)  # 3   — floor division (rounds down to the nearest whole number)\n'
                    'print(a % b)   # 1   — modulus (the remainder after division)\n'
                    'print(a ** b)  # 1000 — exponentiation (10 to the power of 3)\n\n'
                    "Two of these are worth highlighting. Floor division (//) divides and drops the decimal, giving you a whole number — useful when you need a count rather than a precise value. Modulus (%) gives you the remainder after division, which comes up more often than you'd think; a classic use is checking whether a number is even or odd: if number % 2 == 0, it's even."
                ),
            },
            {
                'title': 'Booleans',
                'body': (
                    "A boolean is the simplest data type in Python. It has exactly two possible values: True or False. That's it.\n\n"
                    'is_logged_in = True\n'
                    'task_completed = False\n\n'
                    "Notice that True and False are capitalized — that's required in Python; true and false in lowercase will cause an error.\n\n"
                    "Booleans might seem too simple to be useful on their own, but they're the backbone of decision making in programming. Whenever your code needs to check a condition and decide what to do next, it's working with booleans behind the scenes. Comparisons, for example, always produce a boolean result:\n\n"
                    'age = 20\n'
                    'print(age > 18)    # True\n'
                    'print(age == 18)   # False\n'
                    'print(age != 18)   # True\n'
                    'print(age < 18)    # False\n\n'
                    "We'll put booleans to work properly in the next section when we cover if statements and logic. For now, just know what they are and that they represent a true or false state."
                ),
            },
            {
                'title': 'Type Checking with type()',
                'body': (
                    "Python is what's called a dynamically typed language. That means you don't have to tell Python what type of data a variable holds — Python figures it out automatically based on the value you assign.\n\n"
                    "But sometimes you want to check what type a variable is, especially when debugging or working with data from an outside source. That's where the built-in type() function comes in.\n\n"
                    'name = "Mike"\n'
                    'age = 44\n'
                    'price = 9.99\n'
                    'is_active = True\n'
                    "print(type(name))       # <class 'str'>\n"
                    "print(type(age))        # <class 'int'>\n"
                    "print(type(price))      # <class 'float'>\n"
                    "print(type(is_active))  # <class 'bool'>\n\n"
                    "The output tells you the class of the value: str for string, int for integer, float for float, and bool for boolean. This is particularly useful when something isn't behaving the way you expect — if a number is stored as a string instead of an integer, math operations won't work correctly, and type() will show you exactly what's going on."
                ),
            },
            {
                'title': 'Type Conversion',
                'body': (
                    "Sometimes you have data stored as one type but need it in another. Python provides built-in functions to convert between types — this is called type conversion, or casting: int(), float(), str(), and bool().\n\n"
                    "Here are some practical examples:\n\n"
                    '# String to integer\n'
                    'age = "44"\n'
                    'age_as_int = int(age)\n'
                    'print(age_as_int + 1)   # 45\n\n'
                    '# Integer to string\n'
                    'score = 100\n'
                    'print("Your score is " + str(score))   # Your score is 100\n\n'
                    '# String to float\n'
                    'price = "9.99"\n'
                    'print(float(price) + 1)   # 10.99\n\n'
                    '# Float to integer (drops the decimal — does not round)\n'
                    'print(int(9.99))   # 9\n\n'
                    "The most common place you'll run into this is with user input. When Python collects input from a user, it always stores it as a string, even if the user typed a number. So if you ask someone for their age and try to do math with it directly, you'll get an error unless you convert it first:\n\n"
                    'age = input("How old are you? ")   # user types 25 — stored as "25"\n'
                    "print(age + 1)                     # ERROR — can't add string and integer\n"
                    'print(int(age) + 1)                # 26 — works correctly after conversion\n\n'
                    "We'll use input() a lot starting in the next section, so getting comfortable with type conversion now will save you a lot of frustration later."
                ),
            },
            {
                'title': 'String Formatting with f-strings',
                'body': (
                    "We've seen that you can combine strings using the + operator. But when you're mixing text and variables together, that approach gets messy quickly:\n\n"
                    'name = "Mike"\n'
                    'age = 44\n'
                    'print("My name is " + name + " and I am " + str(age) + " years old.")\n\n'
                    "That works, but it's hard to read and easy to make mistakes. There's a much cleaner way: f-strings.\n\n"
                    "An f-string starts with the letter f before the opening quote. Inside the string, you can embed variables directly by wrapping them in curly braces:\n\n"
                    'name = "Mike"\n'
                    'age = 44\n'
                    'print(f"My name is {name} and I am {age} years old.")\n\n'
                    'Output:\n'
                    'My name is Mike and I am 44 years old.\n\n'
                    "Python replaces {name} with the value of name and {age} with the value of age automatically — no concatenation, no str() conversion needed. You can put expressions inside the curly braces too:\n\n"
                    'price = 9.99\n'
                    'quantity = 3\n'
                    'print(f"Total: ${price * quantity}")   # Total: $29.97\n\n'
                    "f-strings also give you control over how numbers are displayed:\n\n"
                    'pi = 3.14159265\n'
                    'print(f"Pi is approximately {pi:.2f}")   # Pi is approximately 3.14\n\n'
                    "The :.2f tells Python to display the float with exactly 2 decimal places — useful any time you're displaying prices or measurements. f-strings are the modern, preferred way to format strings in Python, and we'll use them constantly throughout the rest of the course."
                ),
            },
            {
                'title': 'Mini Project: Mad Libs Generator',
                'body': (
                    "You've learned about variables, data types, type conversion, and f-strings. Now let's put them all together in something fun.\n\n"
                    "The challenge: write a script that asks the user for several words — a name, an adjective, a noun, a verb, a place, and a number — stores each in a variable, then uses an f-string to build and print a funny story. Make sure every variable shows up somewhere in the story. Give it a try before looking at the solution below.\n\n"
                    'Solution:\n\n'
                    '# Mad Libs Generator\n'
                    'name = input("Enter a person\'s name: ")\n'
                    'adjective = input("Enter an adjective: ")\n'
                    'noun = input("Enter a noun: ")\n'
                    'verb = input("Enter a verb: ")\n'
                    'place = input("Enter a place: ")\n'
                    'number = input("Enter a number: ")\n\n'
                    'print(f"""\n'
                    'One day, {name} woke up feeling extremely {adjective}.\n'
                    'After eating {number} bowls of cereal, they decided to {verb} all the way to {place}.\n'
                    'When they arrived, they discovered a giant {noun} sitting in the middle of the street.\n'
                    'Nobody knew how it got there. Nobody asked. {name} simply nodded, turned around, and went home.\n'
                    'The end.\n'
                    '""")\n\n'
                    "A couple of things worth noting: the triple-quoted f-string (f\"\"\") lets a string span multiple lines, which makes longer blocks of text much easier to write and read. And since we're only using the user's input as text inside a story, no type conversion is needed here — if we wanted to do math with number we'd need int(number), but here it's just displayed as-is."
                ),
            },
        ],
    },
    {
        'title': 'Section 3: User Input & Basic Logic',
        'goal': 'Make programs that respond to the user.',
        'lectures': [
            {
                'title': 'Getting Input with input()',
                'body': (
                    "So far every program we've written has been one-sided. We write the code, we run it, and it does exactly the same thing every time. That's fine for practice, but real programs need to respond to the person using them — they need to ask questions, receive answers, and do something with what they get back.\n\n"
                    "In Python, we collect input from the user with the built-in input() function:\n\n"
                    'name = input("What is your name? ")\n'
                    'print(f"Hello, {name}!")\n\n'
                    'Output:\n'
                    'What is your name? Mike\n'
                    'Hello, Mike!\n\n'
                    "When Python hits the input() line it pauses, displays the prompt text to the user, and waits. Whatever the user types and presses Enter on gets stored in the variable on the left, and the program continues from there. The prompt text is technically optional, but always include it — without one, the user just stares at a blinking cursor with no idea what to do.\n\n"
                    "The most important thing to know about input(): no matter what the user types, it always returns a string. Always. Even if they type a number.\n\n"
                    'age = input("How old are you? ")\n'
                    "print(type(age))   # <class 'str'>\n\n"
                    "If you need to do math with the value, you have to convert it first using int() or float(), exactly as we covered in the last section:\n\n"
                    'age = int(input("How old are you? "))\n'
                    'print(f"In 10 years you will be {age + 10}.")\n\n'
                    'Output:\n'
                    'How old are you? 25\n'
                    'In 10 years you will be 35.\n\n'
                    "Wrapping int() directly around input() is a very common pattern in Python — it converts the input to an integer in a single line rather than two. Get comfortable with it, because you'll use it constantly."
                ),
            },
            {
                'title': 'Comparing Values',
                'body': (
                    "Now that we can collect input from the user, we need a way to evaluate it. Is the number they entered too high? Is their answer correct? Is their age above a certain threshold? To answer these kinds of questions, Python gives us comparison operators.\n\n"
                    "A comparison always produces a boolean result: either True or False.\n\n"
                    'x = 10\n'
                    'y = 5\n'
                    'print(x == y)   # False — is x equal to y?\n'
                    'print(x != y)   # True  — is x not equal to y?\n'
                    'print(x > y)    # True  — is x greater than y?\n'
                    'print(x < y)    # False — is x less than y?\n'
                    'print(x >= y)   # True  — is x greater than or equal to y?\n'
                    'print(x <= y)   # False — is x less than or equal to y?\n\n'
                    "One thing worth flagging: == checks if two values are equal, using a double equals sign. A single = is for assigning a value; == is for comparing two values. Mixing these up is one of the most common beginner mistakes.\n\n"
                    "Comparisons work on strings too:\n\n"
                    'password = "python123"\n'
                    'guess = input("Enter the password: ")\n'
                    'print(guess == password)   # True if they match, False if not\n\n'
                    "This is the foundation of every decision your programs will make. So let's put it to use."
                ),
            },
            {
                'title': 'if, elif, else',
                'body': (
                    "Comparisons on their own just produce True or False. What makes them powerful is combining them with conditional statements — code that only runs when a certain condition is met.\n\n"
                    "The most fundamental conditional in Python is the if statement:\n\n"
                    'age = int(input("How old are you? "))\n'
                    'if age >= 18:\n'
                    '    print("You are an adult.")\n\n'
                    "Read this exactly as it sounds: \"if age is greater than or equal to 18, print 'You are an adult.'\" If the condition is True, the indented code runs. If it's False, Python skips it entirely and moves on.\n\n"
                    "Indentation matters, a lot. Python uses indentation to define which code belongs to which block. The code inside an if statement must be indented, conventionally by 4 spaces. This is not a style choice — in Python, indentation is part of the syntax. If it's wrong, your program will either crash or behave unexpectedly.\n\n"
                    'if age >= 18:\n'
                    '    print("You are an adult.")      # indented — part of the if block\n'
                    'print("Thanks for using the app.")  # not indented — always runs\n\n'
                    "What if you want something to happen when the condition is False? That's what else is for — it doesn't take a condition, it simply catches everything the if didn't:\n\n"
                    'age = int(input("How old are you? "))\n'
                    'if age >= 18:\n'
                    '    print("You are an adult.")\n'
                    'else:\n'
                    '    print("You are not yet an adult.")\n\n'
                    'What if you have more than two possible outcomes? That\'s where elif comes in, short for "else if." It lets you check additional conditions in sequence:\n\n'
                    'score = int(input("Enter your score: "))\n'
                    'if score >= 90:\n'
                    '    print("Grade: A")\n'
                    'elif score >= 80:\n'
                    '    print("Grade: B")\n'
                    'elif score >= 70:\n'
                    '    print("Grade: C")\n'
                    'else:\n'
                    '    print("Grade: F")\n\n'
                    "Python checks each condition from top to bottom and runs the first one that is True. Once a match is found, the rest are skipped entirely. You can have as many elif branches as you need, and you don't always need an else — but if there's a case your if and elif blocks don't cover, else gives you a safe fallback."
                ),
            },
            {
                'title': 'Combining Conditions with and, or, not',
                'body': (
                    "Sometimes a single comparison isn't enough. What if you need two things to be true at the same time? Or at least one of two things to be true? Python gives us three logical operators for combining conditions: and, or, and not.\n\n"
                    "and requires both conditions to be True for the overall result to be True:\n\n"
                    'age = int(input("How old are you? "))\n'
                    'has_ticket = input("Do you have a ticket? (yes/no) ")\n'
                    'if age >= 18 and has_ticket == "yes":\n'
                    '    print("Welcome! Enjoy the show.")\n'
                    'else:\n'
                    '    print("Sorry, you cannot enter.")\n\n'
                    "Both conditions must be met. If the user is 18 but has no ticket, denied. If they have a ticket but are under 18, denied.\n\n"
                    "or requires at least one condition to be True:\n\n"
                    'day = input("What day is it? ")\n'
                    'if day == "Saturday" or day == "Sunday":\n'
                    '    print("It\'s the weekend!")\n'
                    'else:\n'
                    '    print("It\'s a weekday.")\n\n'
                    "not flips a boolean value — True becomes False and False becomes True. It's used to check that something is NOT the case:\n\n"
                    'is_raining = False\n'
                    'if not is_raining:\n'
                    '    print("Great day for a walk!")\n'
                    'else:\n'
                    '    print("Better bring an umbrella.")\n\n'
                    "You can chain logical operators together for more complex conditions. Use parentheses to make the logic clear:\n\n"
                    'age = int(input("How old are you? "))\n'
                    'is_member = input("Are you a member? (yes/no) ")\n'
                    'has_coupon = input("Do you have a coupon? (yes/no) ")\n'
                    'if age >= 65 or (is_member == "yes" and has_coupon == "yes"):\n'
                    '    print("You qualify for a discount!")\n'
                    'else:\n'
                    '    print("No discount available.")\n\n'
                    "When combining operators, Python evaluates not first, then and, then or, just like order of operations in math. When in doubt, use parentheses to make your intent explicit."
                ),
            },
            {
                'title': 'Mini Project: Number Guessing Game',
                'body': (
                    "You've learned how to collect user input, compare values, and write conditional logic. Let's put it all together in your first interactive game.\n\n"
                    "The challenge: pick a secret number between 1 and 20, ask the user to guess it, and tell them if their guess is too high, too low, or correct, using if, elif, and else.\n\n"
                    "Hint: Python has a built-in module called random that can pick a number for you. Add import random at the top of your script, then secret_number = random.randint(1, 20) gives you a random number between 1 and 20. Don't worry too much about import and modules just yet — we cover them properly later in the course.\n\n"
                    'Solution:\n\n'
                    '# Number Guessing Game\n'
                    'import random\n\n'
                    '# Pick a secret number between 1 and 20\n'
                    'secret_number = random.randint(1, 20)\n\n'
                    '# Ask the user for their guess\n'
                    'guess = int(input("I\'m thinking of a number between 1 and 20. What\'s your guess? "))\n\n'
                    '# Check the guess\n'
                    'if guess == secret_number:\n'
                    '    print(f"That\'s it! The number was {secret_number}. Well done!")\n'
                    'elif guess < secret_number:\n'
                    '    print(f"Too low! The number was {secret_number}. Try again next time.")\n'
                    'elif guess > secret_number:\n'
                    '    print(f"Too high! The number was {secret_number}. Try again next time.")\n\n'
                    "A few things worth noting: import random loads Python's built-in random module so we can use randint(), and imports always go at the very top of the file. random.randint(1, 20) generates a random whole number between 1 and 20, inclusive of both ends. int(input(...)) converts the guess from a string to an integer so it can be compared mathematically. And the secret number is revealed in every outcome message using an f-string, giving the user feedback regardless of whether they got it right."
                ),
            },
        ],
    },
    {
        'title': 'Section 4: Lists & Loops',
        'goal': 'Work with collections of data and repeat actions.',
        'lectures': [
            {
                'title': 'What is a List?',
                'body': (
                    "In every lecture so far, every variable we've created has held a single value — one name, one number, one boolean. That works fine for one piece of data, but what happens when you need to work with many pieces at once? A list of groceries, a collection of scores, a set of usernames?\n\n"
                    "Storing each one in its own variable would be a nightmare:\n\n"
                    'item1 = "Apples"\n'
                    'item2 = "Bread"\n'
                    'item3 = "Milk"\n'
                    'item4 = "Eggs"\n\n'
                    "That's already hard to manage with four items — imagine fifty. Python solves this with a list, a single variable that can hold multiple values in a specific order:\n\n"
                    'shopping_list = ["Apples", "Bread", "Milk", "Eggs"]\n\n'
                    "A list is defined using square brackets with each item separated by a comma. The items inside are called elements. A list can hold any data type, and can even mix types, though in practice you'll usually keep things consistent:\n\n"
                    'mixed = ["Mike", 44, 9.99, True]   # valid, but uncommon\n\n'
                    "You can also create an empty list and add to it later, which we'll do a lot:\n\n"
                    'shopping_list = []'
                ),
            },
            {
                'title': 'Accessing, Adding, and Removing Items',
                'body': (
                    "Every item in a list has a position called an index. Python lists are zero-indexed, meaning the first item is at index 0, the second is at index 1, and so on. You access items by placing the index in square brackets after the list name:\n\n"
                    'shopping_list = ["Apples", "Bread", "Milk", "Eggs"]\n'
                    'print(shopping_list[0])   # Apples\n'
                    'print(shopping_list[3])   # Eggs\n\n'
                    "Zero-indexing catches almost every beginner off guard at least once — the first item is [0], not [1]. Python also supports negative indexing, which lets you count from the end of the list: shopping_list[-1] is always the last item regardless of how long the list is.\n\n"
                    "The len() function returns the number of items in a list: len(shopping_list) is 4.\n\n"
                    "There are two main ways to add items. .append() adds a single item to the end of the list:\n\n"
                    'shopping_list.append("Butter")\n\n'
                    ".insert() adds an item at a specific index, pushing everything else to the right. .append() is by far the more commonly used of the two.\n\n"
                    "For removing items: .remove() removes the first item that matches the value you provide, .pop() removes and returns the item at a specific index (or the last item if none is given), and del removes an item at a specific index without returning it.\n\n"
                    "A few other useful list methods: .sort() sorts the list in place, .reverse() reverses it in place, .count() counts occurrences of a value, and .clear() removes everything.\n\n"
                    "Finally, you can check whether a value exists in a list using the in keyword:\n\n"
                    'shopping_list = ["Apples", "Bread", "Milk"]\n'
                    'print("Milk" in shopping_list)    # True\n'
                    'print("Butter" in shopping_list)  # False\n\n'
                    "This will come in very handy once we start writing logic around our lists."
                ),
            },
            {
                'title': 'for Loops',
                'body': (
                    "We now know how to store multiple items in a list, but how do we do something with each one? We could access them one by one using their index, but that doesn't scale — if the list has a hundred items, we're not writing a hundred lines of code.\n\n"
                    "This is exactly what loops are for. A loop lets you repeat a block of code automatically, either for each item in a collection, or until a condition is no longer true. The first type is the for loop, which iterates over a list and runs the indented code once for each item:\n\n"
                    'shopping_list = ["Apples", "Bread", "Milk", "Eggs"]\n'
                    'for item in shopping_list:\n'
                    '    print(item)\n\n'
                    "Read this as: \"for each item in shopping_list, print that item.\" Python goes through the list from start to finish, assigns each element to the variable item one at a time, and runs the code block for each one. The variable name after for is up to you — item, i, element — whatever makes sense for the context.\n\n"
                    "The code inside the loop can be as complex as you need:\n\n"
                    'prices = [2.99, 5.49, 1.25, 8.00]\n'
                    'total = 0\n'
                    'for price in prices:\n'
                    '    total = total + price\n'
                    'print(f"Total: ${total:.2f}")   # Total: $17.73\n\n'
                    "This pattern — starting with a variable outside the loop and updating it on each pass — is one of the most fundamental patterns in programming. You'll use it constantly.\n\n"
                    "Sometimes you need both the item and its index position. enumerate() gives you both:\n\n"
                    'shopping_list = ["Apples", "Bread", "Milk", "Eggs"]\n'
                    'for index, item in enumerate(shopping_list):\n'
                    '    print(f"{index + 1}. {item}")\n\n'
                    "We use index + 1 here because zero-indexing would make a list displayed to a user start at 0, which looks odd."
                ),
            },
            {
                'title': 'while Loops',
                'body': (
                    "The for loop is perfect when you know what you're iterating over. But sometimes you don't know in advance how many times a loop should run — you just know it should keep going until something changes. That's what the while loop is for.\n\n"
                    "A while loop keeps running as long as its condition is True:\n\n"
                    'count = 1\n'
                    'while count <= 5:\n'
                    '    print(f"Count: {count}")\n'
                    '    count = count + 1\n\n'
                    "Read this as: \"while count is less than or equal to 5, print the count and then add 1 to it.\" Once count reaches 6, the condition becomes False and the loop stops.\n\n"
                    "The most important rule with while loops: you must make sure the condition eventually becomes False. If it never does, the loop runs forever — this is called an infinite loop, and it will freeze your program.\n\n"
                    '# DANGER — infinite loop\n'
                    'while True:\n'
                    '    print("This never stops!")\n\n'
                    "Always make sure something inside your loop is working toward ending the condition. In the earlier example, count = count + 1 is what eventually makes count <= 5 become False.\n\n"
                    "A very common use of while loops is keeping a program running until the user decides to quit:\n\n"
                    'running = True\n'
                    'while running:\n'
                    '    answer = input("Keep going? (yes/no) ")\n'
                    '    if answer == "no":\n'
                    '        running = False\n'
                    'print("Program ended.")\n\n'
                    "This pattern — a loop that continues until a user triggers an exit condition — is the backbone of interactive terminal programs. We'll use it in the mini project."
                ),
            },
            {
                'title': 'range()',
                'body': (
                    "When you need to loop a specific number of times but don't have a list to iterate over, Python's built-in range() function generates a sequence of numbers for you.\n\n"
                    'for i in range(5):\n'
                    '    print(i)\n\n'
                    "Output: 0, 1, 2, 3, 4. range(5) generates five numbers total, starting at 0 — just like list indexing, range() starts at zero by default.\n\n"
                    "You can specify where range() starts and stops. The start is inclusive, the stop is exclusive, meaning Python goes up to but doesn't include the stop value:\n\n"
                    'for i in range(1, 6):\n'
                    '    print(i)   # 1, 2, 3, 4, 5\n\n'
                    "A third argument controls the step — how much to increment by on each pass:\n\n"
                    'for i in range(0, 20, 5):\n'
                    '    print(i)   # 0, 5, 10, 15\n\n'
                    "You can also step backwards using a negative value: range(10, 0, -1) counts down from 10 to 1."
                ),
            },
            {
                'title': 'break and continue',
                'body': (
                    "Sometimes you need more control over how a loop runs — the ability to exit it early or skip a particular iteration. Python gives you two tools for this: break and continue.\n\n"
                    "break immediately exits the loop, regardless of whether the condition is still true or there are items left to iterate over:\n\n"
                    'numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n'
                    'for number in numbers:\n'
                    '    if number == 5:\n'
                    '        break\n'
                    '    print(number)   # prints 1, 2, 3, 4\n\n'
                    "The moment number equals 5, break fires and the loop ends — 5 itself never gets printed because break triggers before the print() line. break is commonly used to exit a while loop when a certain condition is met:\n\n"
                    'while True:\n'
                    '    guess = input("Guess the secret word: ")\n'
                    '    if guess == "python":\n'
                    '        print("Correct!")\n'
                    '        break\n'
                    '    print("Wrong, try again.")\n\n'
                    "Here the loop runs indefinitely (while True), but break gives us a clean exit when the user gets it right.\n\n"
                    "continue skips the rest of the current iteration and jumps straight to the next one — the loop doesn't end, it just moves on:\n\n"
                    'numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n'
                    'for number in numbers:\n'
                    '    if number % 2 == 0:\n'
                    '        continue\n'
                    '    print(number)   # prints only the odd numbers\n\n'
                    "When number % 2 == 0 is True, meaning the number is even, continue skips the print() and moves to the next number."
                ),
            },
            {
                'title': 'Mini Project: Shopping List App',
                'body': (
                    "You've learned about lists, for loops, while loops, range(), break, and continue. Now let's build something genuinely useful that puts all of it together.\n\n"
                    "The challenge: build a shopping list app that starts with an empty list and shows a menu with four options — add an item, view the list, remove an item, and quit — repeating the menu after each action until the user quits. Numbered items should start from 1, not 0, and you should handle the case where the list is empty when viewing or removing.\n\n"
                    'Solution:\n\n'
                    '# Shopping List App\n'
                    'shopping_list = []\n\n'
                    'while True:\n'
                    '    print("\\n-- Shopping List --")\n'
                    '    print("1. Add item")\n'
                    '    print("2. View list")\n'
                    '    print("3. Remove item")\n'
                    '    print("4. Quit")\n'
                    '    choice = input("\\nChoose an option (1-4): ")\n\n'
                    '    if choice == "1":\n'
                    '        item = input("Enter the item to add: ")\n'
                    '        shopping_list.append(item)\n'
                    '        print(f"\'{item}\' has been added to your list.")\n'
                    '    elif choice == "2":\n'
                    '        if len(shopping_list) == 0:\n'
                    '            print("Your list is empty.")\n'
                    '        else:\n'
                    '            for index, item in enumerate(shopping_list):\n'
                    '                print(f"  {index + 1}. {item}")\n'
                    '    elif choice == "3":\n'
                    '        if len(shopping_list) == 0:\n'
                    '            print("Your list is empty — nothing to remove.")\n'
                    '        else:\n'
                    '            item = input("Enter the item to remove: ")\n'
                    '            if item in shopping_list:\n'
                    '                shopping_list.remove(item)\n'
                    '                print(f"\'{item}\' has been removed.")\n'
                    '            else:\n'
                    '                print(f"\'{item}\' was not found in your list.")\n'
                    '    elif choice == "4":\n'
                    '        print("Goodbye! Happy shopping.")\n'
                    '        break\n'
                    '    else:\n'
                    '        print("Invalid option. Please choose 1, 2, 3, or 4.")\n\n'
                    "A few things worth noting: while True runs indefinitely, keeping the menu on screen after every action — the only way out is the break in option 4. len(shopping_list) == 0 checks whether the list is empty before trying to display or remove items, avoiding confusing output or errors. enumerate() gives us both the index and item so we can display a numbered list starting from 1. And item in shopping_list checks whether the item actually exists before calling .remove(), since removing something that isn't there would raise an error."
                ),
            },
        ],
    },
    {
        'title': 'Section 5: Dictionaries & Tuples',
        'goal': 'Understand more complex data structures.',
        'lectures': [
            {
                'title': 'What is a Dictionary?',
                'body': (
                    "We learned that a list is great for storing a collection of items in order. But lists have a limitation: the only way to identify an item is by its position. If you want to store information about something, like a person's name, phone number, and email address, a list starts to feel awkward:\n\n"
                    'contact = ["Mike", "555-1234", "msmith@example.com"]\n\n'
                    "To get the phone number you'd have to remember that it's at index 1. That's fragile and hard to read. A dictionary solves this by letting you store data as key-value pairs instead of positional items. Rather than accessing data by index, you access it by a meaningful name — the key:\n\n"
                    'contact = {\n'
                    '    "name": "Mike",\n'
                    '    "phone": "555-1234",\n'
                    '    "email": "msmith@example.com"\n'
                    '}\n\n'
                    'Now instead of contact[1] you write contact["phone"], which is immediately clear to anyone reading the code.\n\n'
                    "A dictionary is defined using curly braces. Each entry is a key-value pair separated by a colon, and pairs are separated by commas. The key is almost always a string; the value can be anything — a string, integer, float, boolean, list, or even another dictionary.\n\n"
                    'person = {\n'
                    '    "name": "Sarah",\n'
                    '    "age": 28,\n'
                    '    "is_member": True,\n'
                    '    "scores": [95, 87, 92]\n'
                    '}\n\n'
                    'print(person["name"])      # Sarah\n'
                    'print(person["scores"])    # [95, 87, 92]\n\n'
                    "You can also use the .get() method to access a value. The difference is that if the key doesn't exist, .get() returns None instead of throwing an error:\n\n"
                    'print(person.get("email"))          # None\n'
                    'print(person.get("email", "N/A"))   # N/A — default value if key not found\n\n'
                    "The second argument to .get() is an optional default value. This is a safer way to access dictionary values when you're not certain the key exists."
                ),
            },
            {
                'title': 'Adding, Updating, and Deleting Key-Value Pairs',
                'body': (
                    "Dictionaries are mutable, meaning you can change them after they're created. This makes them flexible containers for data that evolves over time.\n\n"
                    "To add a new key-value pair, simply assign a value to a new key. If the key already exists, this same syntax updates the value instead of adding a duplicate:\n\n"
                    'contact = {"name": "Mike", "phone": "555-1234"}\n'
                    'contact["email"] = "msmith@example.com"\n'
                    'contact["phone"] = "555-9999"   # updates the existing value\n\n'
                    "You can also use the .update() method to change multiple values at once:\n\n"
                    'contact.update({"phone": "555-0000", "email": "newemail@example.com"})\n\n'
                    "To delete a key-value pair, use the del keyword to remove a specific key and its value, or .pop() to remove a key and return its value at the same time:\n\n"
                    'del contact["email"]\n'
                    'removed = contact.pop("phone")\n'
                    'print(removed)    # 555-9999\n\n'
                    ".pop() is useful when you need to remove a key but also want to use its value before it's gone. To remove everything, use .clear().\n\n"
                    "Just like lists, you can use in to check whether a key exists in a dictionary before accessing it directly — this is a good habit that prevents your program from crashing if the key isn't there:\n\n"
                    'if "email" in contact:\n'
                    '    print(contact["email"])\n'
                    'else:\n'
                    '    print("No email on file.")'
                ),
            },
            {
                'title': 'Looping Through Dictionaries',
                'body': (
                    "Just like lists, dictionaries can be looped through. There are three ways to do it depending on what you need.\n\n"
                    "By default, looping through a dictionary gives you the keys:\n\n"
                    'contact = {"name": "Mike", "phone": "555-1234", "email": "msmith@example.com"}\n'
                    'for key in contact:\n'
                    '    print(key)   # name, phone, email\n\n'
                    "Use .values() to loop through just the values:\n\n"
                    'for value in contact.values():\n'
                    '    print(value)   # Mike, 555-1234, msmith@example.com\n\n'
                    "And use .items() to get both at the same time — this is the most commonly used approach:\n\n"
                    'for key, value in contact.items():\n'
                    '    print(f"{key}: {value}")\n\n'
                    "Output:\n"
                    "name: Mike\n"
                    "phone: 555-1234\n"
                    "email: msmith@example.com\n\n"
                    ".items() returns each key-value pair as a tuple, which leads us perfectly into the next lecture."
                ),
            },
            {
                'title': 'What is a Tuple and When to Use It',
                'body': (
                    "A tuple is a data structure that looks a lot like a list — it holds an ordered collection of items. The key difference is that a tuple is immutable, meaning once it's created it cannot be changed. You can't add to it, remove from it, or modify any of its values.\n\n"
                    "A tuple is defined using parentheses instead of square brackets:\n\n"
                    'coordinates = (40.7128, -74.0060)\n'
                    'rgb = (255, 128, 0)\n\n'
                    "You access items the same way as a list, by index, and you can loop through a tuple just like a list.\n\n"
                    "Why use a tuple if a list does more? A few good reasons. Immutability is intentional — using a tuple signals to anyone reading your code, including your future self, that this data should not change. Geographic coordinates, screen dimensions, and RGB color values don't need to be modified, and a tuple enforces that. Tuples are also faster, since Python knows they can never change, it can store and access them more efficiently. And tuples can be dictionary keys, while lists cannot, because lists are mutable:\n\n"
                    'locations = {\n'
                    '    (40.7128, -74.0060): "New York",\n'
                    '    (51.5074, -0.1278): "London"\n'
                    '}\n\n'
                    "In practice, use a list when the data might change and a tuple when it shouldn't.\n\n"
                    "One very common use of tuples is unpacking — assigning each value in a tuple to its own variable in a single line:\n\n"
                    'coordinates = (40.7128, -74.0060)\n'
                    'latitude, longitude = coordinates\n\n'
                    "You've actually already seen this in action: for key, value in contact.items() is tuple unpacking. Each key-value pair is a tuple, and we unpack it directly in the loop."
                ),
            },
            {
                'title': 'Nested Data Structures',
                'body': (
                    "So far we've worked with lists of strings and dictionaries with simple values. But in the real world, data is rarely that flat. A contact book doesn't just have one contact, it has many. This is where nesting comes in — placing one data structure inside another: a list of dictionaries, a dictionary of lists, a dictionary of dictionaries. Python handles all of these naturally.\n\n"
                    "A list of dictionaries is one of the most common patterns you'll encounter, and the one we'll use in our mini project:\n\n"
                    'contacts = [\n'
                    '    {"name": "Mike", "phone": "555-1234"},\n'
                    '    {"name": "Sarah", "phone": "555-5678"},\n'
                    ']\n\n'
                    "Each item in the list is a dictionary. To access a specific contact's phone number: contacts[0][\"phone\"]. To loop through all contacts:\n\n"
                    'for contact in contacts:\n'
                    '    print(f"{contact[\'name\']}: {contact[\'phone\']}")\n\n'
                    "A dictionary of dictionaries is another common pattern, useful when each entry has a natural unique identifier, like a username:\n\n"
                    'contacts = {\n'
                    '    "mike": {"phone": "555-1234", "email": "mike@example.com"},\n'
                    '    "sarah": {"phone": "555-5678", "email": "sarah@example.com"}\n'
                    '}\n'
                    'print(contacts["mike"]["email"])\n\n'
                    "And a dictionary can hold a list as a value too:\n\n"
                    'person = {"name": "Mike", "hobbies": ["coding", "reading", "hiking"]}\n'
                    'for hobby in person["hobbies"]:\n'
                    '    print(hobby)\n\n'
                    "Nesting lets you model real-world data naturally. As your programs grow more complex you'll reach for these patterns constantly, and you'll also see them everywhere in Django, where data from a database often comes back as a list of dictionaries."
                ),
            },
            {
                'title': 'Mini Project: Contact Book',
                'body': (
                    "You've learned about dictionaries, tuples, and nested data structures. Now let's build a contact book that puts them all to work.\n\n"
                    "The challenge: store contacts as a dictionary where each contact has a name and phone number, with a menu offering add, view all, look up by name, and quit. Handle the case where the contact book is empty.\n\n"
                    'Solution:\n\n'
                    '# Contact Book\n'
                    'contacts = {}\n\n'
                    'while True:\n'
                    '    print("\\n-- Contact Book --")\n'
                    '    print("1. Add a contact")\n'
                    '    print("2. View all contacts")\n'
                    '    print("3. Look up a contact")\n'
                    '    print("4. Quit")\n'
                    '    choice = input("\\nChoose an option (1-4): ")\n\n'
                    '    if choice == "1":\n'
                    '        name = input("Enter the contact\'s name: ").title()\n'
                    '        phone = input(f"Enter {name}\'s phone number: ")\n'
                    '        contacts[name] = {"phone": phone}\n'
                    '        print(f"\'{name}\' has been added to your contact book.")\n'
                    '    elif choice == "2":\n'
                    '        if len(contacts) == 0:\n'
                    '            print("Your contact book is empty.")\n'
                    '        else:\n'
                    '            for name, details in contacts.items():\n'
                    "                print(f\"  {name}: {details['phone']}\")\n"
                    '    elif choice == "3":\n'
                    '        if len(contacts) == 0:\n'
                    '            print("Your contact book is empty.")\n'
                    '        else:\n'
                    '            name = input("Enter the name to look up: ").title()\n'
                    '            if name in contacts:\n'
                    "                print(f\"Phone: {contacts[name]['phone']}\")\n"
                    '            else:\n'
                    '                print(f"No contact found for \'{name}\'.")\n'
                    '    elif choice == "4":\n'
                    '        print("Goodbye!")\n'
                    '        break\n'
                    '    else:\n'
                    '        print("Invalid option. Please choose 1, 2, 3, or 4.")\n\n'
                    'A few things worth noting: we start with an empty dictionary, contacts = {}, where each contact is added as a key-value pair — the key is the name, the value is another dictionary holding their details. .title() is called on the name input to capitalize it consistently, so "mike", "Mike", and "MIKE" all get stored and looked up as "Mike," preventing duplicate entries from inconsistent capitalization. And "if name in contacts" checks whether the name exists before trying to access it, so looking up someone who was never added doesn\'t crash the program.'
                ),
            },
        ],
    },
    {
        'title': 'Section 6: Functions',
        'goal': 'Write reusable, organized code.',
        'lectures': [
            {
                'title': 'What is a Function and Why Use It?',
                'body': (
                    "Take a look at the mini projects we've built so far. Each one has a while True loop, a menu, and blocks of code handling each option. As programs grow, you start to notice something: you're writing the same logic in multiple places. You're repeating yourself, and every time you need to change something, you have to find and update every place it appears.\n\n"
                    "Functions solve this problem. A function is a named, reusable block of code that performs a specific task. You define it once and call it as many times as you need, from anywhere in your program. You've already been using functions this entire course — print(), input(), len(), int(), range() are all built-in Python functions. Now we're going to learn how to write our own.\n\n"
                    "Why does this matter? Reusability — write the logic once, use it everywhere, and if something needs to change, you change it in one place and it's fixed everywhere. Readability — a well-named function makes your code read almost like plain English; calculate_total() tells you exactly what that block of code does without reading every line inside it. And organization — functions break a large program into smaller, focused pieces, each with one job, making your code easier to write, read, and fix.\n\n"
                    "This is one of the most important concepts in programming. Everything from here forward, including high-level, pre-built frameworks like Django, is built on functions."
                ),
            },
            {
                'title': 'Defining and Calling Functions',
                'body': (
                    "In Python, you define a function using the def keyword followed by the function name, a pair of parentheses, and a colon. The code inside is indented, just like if statements and loops.\n\n"
                    'def greet():\n'
                    '    print("Hello! Welcome to Python.")\n\n'
                    "This defines the function but doesn't run it. Defining a function is like writing a recipe — the recipe exists, but nothing gets cooked until you actually use it. To run the code inside, you call it by writing its name followed by parentheses:\n\n"
                    'greet()\n'
                    'greet()\n'
                    'greet()\n\n'
                    "Three calls, one definition. That's the power of reusability.\n\n"
                    "Function names follow the same rules as variable names: lowercase, snake_case, descriptive. A good function name describes what the function does, usually as a verb or verb phrase:\n\n"
                    'def display_menu():       # good\n'
                    'def calculate_total():    # good\n'
                    'def m():                  # bad — too vague\n\n'
                    "A function with a clear, descriptive name makes your code self-documenting. Someone reading calculate_total() knows exactly what to expect without looking inside."
                ),
            },
            {
                'title': 'Parameters and Arguments',
                'body': (
                    "Our greet() function always prints the exact same thing. That's fine for a fixed message, but most functions need to work with different data each time they're called. This is where parameters come in.\n\n"
                    "A parameter is a variable defined inside the function's parentheses — a placeholder for a value that will be passed in when the function is called:\n\n"
                    'def greet(name):\n'
                    '    print(f"Hello, {name}! Welcome to Python.")\n\n'
                    "The value you pass when calling the function is called an argument:\n\n"
                    'greet("Mike")\n'
                    'greet("Sarah")\n\n'
                    "The same function, different results each time. A function can accept as many parameters as it needs, separated by commas:\n\n"
                    'def describe_person(name, age, city):\n'
                    '    print(f"{name} is {age} years old and lives in {city}.")\n\n'
                    'describe_person("Mike", 44, "Boston")\n\n'
                    "When calling a function with multiple arguments, the order matters — Python matches arguments to parameters by position. You can also pass arguments by name, called keyword arguments, which lets you provide them in any order:\n\n"
                    'describe_person(age=44, city="Boston", name="Mike")\n\n'
                    "This produces the same result as before. Keyword arguments make function calls more readable when there are several parameters and the order might not be obvious."
                ),
            },
            {
                'title': 'Return Values',
                'body': (
                    "So far our functions have done things — printed output, displayed menus. But functions can also return a value back to the caller. This is what makes functions truly powerful: they can compute something and hand the result back for use elsewhere in your program.\n\n"
                    "You return a value using the return keyword:\n\n"
                    'def add(a, b):\n'
                    '    return a + b\n\n'
                    'result = add(10, 5)\n'
                    'print(result)   # 15\n\n'
                    "The returned value can be stored in a variable, used in an expression, or passed directly to another function. As soon as Python hits a return statement, it exits the function immediately — any code after return in the same function will not run:\n\n"
                    'def check_age(age):\n'
                    '    if age >= 18:\n'
                    '        return "Adult"\n'
                    '    return "Minor"\n\n'
                    'print(check_age(25))   # Adult\n'
                    'print(check_age(15))   # Minor\n\n'
                    "When age >= 18 is True, the function returns \"Adult\" and exits immediately. The second return is only reached if the first condition was False — a clean way to write functions with multiple possible outcomes without needing elif or else.\n\n"
                    "A function can also return more than one value by separating them with a comma — Python packages them as a tuple:\n\n"
                    'def min_max(numbers):\n'
                    '    return min(numbers), max(numbers)\n\n'
                    'lowest, highest = min_max([3, 1, 7, 2, 9, 4])\n'
                    'print(lowest)    # 1\n'
                    'print(highest)   # 9\n\n'
                    "We unpack the returned tuple directly into two variables — a pattern that feels elegant once you get used to it, and one we'll use in this section's mini project."
                ),
            },
            {
                'title': 'Default Parameters',
                'body': (
                    "Sometimes a function has a parameter that will almost always receive the same value. Requiring the caller to provide it every time is repetitive. Python lets you define a default value for a parameter — if no argument is provided, the default is used automatically.\n\n"
                    'def greet(name, greeting="Hello"):\n'
                    '    print(f"{greeting}, {name}!")\n\n'
                    'greet("Mike")              # Hello, Mike!\n'
                    'greet("Sarah", "Welcome")  # Welcome, Sarah!\n\n'
                    "When greet(\"Mike\") is called without a second argument, greeting falls back to \"Hello.\" When a second argument is provided, it overrides the default.\n\n"
                    "Important rule: parameters with default values must always come after parameters without defaults. This is required by Python, otherwise it wouldn't know which arguments map to which parameters:\n\n"
                    '# Correct\n'
                    'def greet(name, greeting="Hello"):\n'
                    '    ...\n\n'
                    '# Incorrect — will cause an error\n'
                    'def greet(greeting="Hello", name):\n'
                    '    ...\n\n'
                    "Default parameters are great for optional settings — things like tip percentages, tax rates, or display preferences where you want a sensible fallback but still allow customization."
                ),
            },
            {
                'title': 'Variable Scope',
                'body': (
                    "When you create a variable inside a function, it only exists inside that function. Once the function finishes running, the variable is gone. This concept is called scope — the region of your program where a variable can be accessed.\n\n"
                    "A variable created inside a function is local to that function and cannot be accessed from outside:\n\n"
                    'def calculate():\n'
                    '    result = 100\n'
                    '    print(result)   # works fine inside the function\n\n'
                    'calculate()\n'
                    'print(result)   # ERROR — result does not exist out here\n\n'
                    "A variable created outside any function is global, and can be read from anywhere in the program:\n\n"
                    'tax_rate = 0.08   # global variable\n\n'
                    'def calculate_tax(price):\n'
                    '    return price * tax_rate   # reads the global tax_rate\n\n'
                    "By default, a function can read a global variable but cannot modify it — if you try, Python creates a new local variable with the same name instead. To actually modify a global variable from inside a function, you need to declare it with the global keyword:\n\n"
                    'count = 0\n\n'
                    'def increment():\n'
                    '    global count\n'
                    '    count = count + 1\n\n'
                    'increment()\n'
                    'increment()\n'
                    'print(count)   # 2\n\n'
                    "That said, modifying global variables inside functions is generally considered bad practice — it makes programs harder to follow because any function could be changing the value at any time. A better approach is to pass the variable in as an argument and return the updated value.\n\n"
                    "Scope keeps functions self-contained and predictable. A function that only works with its own local variables and parameters will always behave the same way regardless of what's happening elsewhere in the program — that predictability is what makes functions safe to reuse."
                ),
            },
            {
                'title': 'Mini Project: Tip Calculator',
                'body': (
                    "You've learned how to define functions, work with parameters, return values, set defaults, and understand scope. Now let's build something practical that puts it all together.\n\n"
                    "The challenge: write a function that takes the bill amount and tip percentage as parameters and returns both the tip amount and total, with a default tip of 20%. Ask the user for the bill amount and optionally a custom tip percentage, and offer to split the total among a number of people.\n\n"
                    'Solution:\n\n'
                    '# Tip Calculator\n'
                    'def calculate_tip(bill_amount, tip_percent=20):\n'
                    '    tip_amount = bill_amount * (tip_percent / 100)\n'
                    '    total = bill_amount + tip_amount\n'
                    '    return tip_amount, total\n\n'
                    'def split_bill(total, num_people):\n'
                    '    return total / num_people\n\n'
                    'bill = float(input("Enter the bill amount: $"))\n'
                    'tip_input = input("Enter tip percentage (press Enter for 20%): ")\n\n'
                    'if tip_input == "":\n'
                    '    tip_percent = 20\n'
                    'else:\n'
                    '    tip_percent = float(tip_input)\n\n'
                    'tip_amount, total = calculate_tip(bill, tip_percent)\n\n'
                    'print(f"\\n--- Tip Calculator ---")\n'
                    'print(f"Bill Amount:  ${bill:.2f}")\n'
                    'print(f"Tip ({tip_percent}%):   ${tip_amount:.2f}")\n'
                    'print(f"Total:        ${total:.2f}")\n\n'
                    'split_input = input("\\nSplit the bill? Enter number of people (or press Enter to skip): ")\n'
                    'if split_input != "":\n'
                    '    num_people = int(split_input)\n'
                    '    per_person = split_bill(total, num_people)\n'
                    '    print(f"Each person pays: ${per_person:.2f}")\n\n'
                    'print("\\nEnjoy your meal!")\n\n'
                    'A few things worth noting: tip_percent=20 is a default parameter, so if the user skips the tip input, 20% is used automatically. return tip_amount, total returns two values as a tuple, unpacked directly into two variables on the calling line. split_bill() is a second, focused function with one clear job, kept separate to stay organized and reusable. And {bill:.2f} ensures all money values are displayed with exactly two decimal places, for a clean, professional look.'
                ),
            },
        ],
    },
    {
        'title': 'Section 7: Error Handling',
        'goal': 'Write code that handles mistakes gracefully.',
        'lectures': [
            {
                'title': 'What are Errors and Exceptions?',
                'body': (
                    "Up to this point, whenever something has gone wrong in our programs — a wrong data type, a missing key, a bad conversion — the program has crashed. Python prints a red error message and stops completely. For a learning exercise that's fine, but for a real program that other people are using, crashing is not acceptable. A user who types a letter where a number was expected shouldn't see a wall of error text and a dead program — they should see a helpful message and get another chance.\n\n"
                    "This is what error handling is for. Before we can handle errors, though, we need to understand what they actually are. In Python there are two broad categories of problems.\n\n"
                    "Syntax errors occur when Python can't even parse your code because it's written incorrectly — a missing colon, an unclosed bracket, a misspelled keyword. Python catches these before the program runs at all:\n\n"
                    'if age > 18\n'
                    '    print("Adult")   # SyntaxError: expected \':\'\n\n'
                    "There's no way to handle a syntax error at runtime — you just have to fix it before running the program.\n\n"
                    "Exceptions are different. These are errors that occur while the program is running — the syntax is fine, but something goes wrong during execution. A user enters unexpected input, a calculation produces an impossible result, a file doesn't exist. These are the errors we can catch and handle gracefully:\n\n"
                    'number = int("hello")   # ValueError: invalid literal for int()\n\n'
                    "Python uses the term exception for these runtime errors, and handling them is called exception handling. Learning to anticipate where things can go wrong and writing code that responds intelligently is one of the marks of a good programmer."
                ),
            },
            {
                'title': 'Common Error Types',
                'body': (
                    "Python has many built-in exception types, each describing a specific kind of problem. Knowing the most common ones helps you anticipate what might go wrong and write better error handling.\n\n"
                    "ValueError is raised when a function receives an argument of the right type but an inappropriate value:\n\n"
                    'int("hello")      # ValueError - "hello" can\'t be converted to int\n'
                    'float("abc")      # ValueError - "abc" can\'t be converted to float\n\n'
                    "This is the most common exception you'll encounter when working with user input, since input() always returns a string and users don't always type what you expect.\n\n"
                    "TypeError is raised when an operation is applied to a value of the wrong type:\n\n"
                    '"hello" + 5         # TypeError - can\'t concatenate str and int\n'
                    'len(42)             # TypeError - int has no len()\n\n'
                    "IndexError is raised when you try to access a list index that doesn't exist:\n\n"
                    'numbers = [1, 2, 3]\n'
                    'print(numbers[5])   # IndexError - list only has indices 0, 1, 2\n\n'
                    "KeyError is raised when you try to access a dictionary key that doesn't exist:\n\n"
                    'contact = {"name": "Mike"}\n'
                    'print(contact["email"])   # KeyError - "email" key doesn\'t exist\n\n'
                    "ZeroDivisionError is raised when you try to divide a number by zero:\n\n"
                    'result = 10 / 0   # ZeroDivisionError - division by zero is undefined\n\n'
                    "FileNotFoundError is raised when you try to open a file that doesn't exist — we'll encounter this one properly in Section 9 when we cover file handling:\n\n"
                    'file = open("missing.txt")   # FileNotFoundError - file doesn\'t exist\n\n'
                    "NameError is raised when you try to use a variable that hasn't been defined yet:\n\n"
                    'print(total)   # NameError - total hasn\'t been assigned a value\n\n'
                    "Knowing these by name means when you see one in your terminal you immediately understand what went wrong and where to look. Now let's learn how to catch them."
                ),
            },
            {
                'title': 'try and except',
                'body': (
                    "The primary tool for handling exceptions in Python is the try/except block. The idea is simple: you put the code that might fail inside a try block, and you put the code that should run if it fails inside an except block.\n\n"
                    'try:\n'
                    '    number = int(input("Enter a number: "))\n'
                    '    print(f"You entered: {number}")\n'
                    'except ValueError:\n'
                    '    print("That\'s not a valid number. Please try again.")\n\n'
                    "Here's what happens: Python runs the code inside try. If no exception occurs, the except block is skipped entirely. If a ValueError occurs — meaning the user typed something that can't be converted to an integer — Python immediately jumps to the except block and runs it instead. Either way, the program keeps running. It doesn't crash.\n\n"
                    "You should always try to catch specific exception types rather than catching everything blindly. This way you know exactly what went wrong and can respond appropriately:\n\n"
                    'numbers = [1, 2, 3]\n'
                    'try:\n'
                    '    index = int(input("Enter an index: "))\n'
                    '    print(numbers[index])\n'
                    'except ValueError:\n'
                    '    print("Please enter a whole number.")\n'
                    'except IndexError:\n'
                    '    print(f"Index out of range. The list only has {len(numbers)} items.")\n\n'
                    "You can stack as many except blocks as you need. Python checks them in order and runs the first one that matches the exception type. If you want to handle several exception types the same way, you can group them in a tuple:\n\n"
                    'try:\n'
                    '    result = int(input("Enter a number: ")) / int(input("Divide by: "))\n'
                    '    print(f"Result: {result}")\n'
                    'except (ValueError, ZeroDivisionError):\n'
                    '    print("Invalid input. Please enter non-zero whole numbers.")\n\n'
                    "You can write except without specifying an exception type, and it will catch absolutely everything. This works, but it's considered bad practice — it catches every possible exception, including ones you didn't anticipate and probably shouldn't be silently swallowing. A bare except can hide real bugs in your code and make them very hard to find. Always be specific about what you're catching."
                ),
            },
            {
                'title': 'else and finally',
                'body': (
                    "The try/except block has two optional additions that give you even more control over what happens: else and finally.\n\n"
                    "The else block runs only if the try block completed successfully, meaning no exception was raised. It's the \"everything went fine\" branch:\n\n"
                    'try:\n'
                    '    number = int(input("Enter a number: "))\n'
                    'except ValueError:\n'
                    '    print("That\'s not a valid number.")\n'
                    'else:\n'
                    '    print(f"Great! You entered {number}.")\n'
                    '    print("No errors occurred.")\n\n'
                    "You might wonder why not just put the else code at the end of the try block. The reason is clarity and precision: code in else only runs when the try succeeded, whereas code at the bottom of a try block could theoretically raise its own exception. Keeping them separate makes your intent explicit.\n\n"
                    "The finally block always runs, regardless of whether an exception occurred or not. It's the \"no matter what happens, do this\" block:\n\n"
                    'try:\n'
                    '    number = int(input("Enter a number: "))\n'
                    'except ValueError:\n'
                    '    print("That\'s not a valid number.")\n'
                    'else:\n'
                    '    print(f"You entered {number}.")\n'
                    'finally:\n'
                    '    print("Thank you for using the program.")\n\n'
                    "finally always runs. This makes it perfect for cleanup tasks that need to happen regardless of the outcome — closing a file, closing a database connection, or displaying a farewell message. We'll see a real-world use of finally in Section 9 when we work with files.\n\n"
                    "Here's the full structure with all four blocks working together:\n\n"
                    'try:\n'
                    '    number = int(input("Enter a number: "))\n'
                    '    result = 100 / number\n'
                    'except ValueError:\n'
                    '    print("Please enter a whole number.")\n'
                    'except ZeroDivisionError:\n'
                    '    print("You can\'t divide by zero.")\n'
                    'else:\n'
                    '    print(f"100 divided by {number} is {result:.2f}")\n'
                    'finally:\n'
                    '    print("Calculation complete.")\n\n'
                    "Read it as: \"try this, if this specific thing goes wrong do that, if this other thing goes wrong do that, if nothing went wrong do this, and always do this at the end.\""
                ),
            },
            {
                'title': 'Raising Your Own Errors',
                'body': (
                    "So far we've been catching exceptions that Python raises automatically. But you can also raise exceptions yourself, deliberately triggering an error when your code encounters a situation it considers invalid. You do this with the raise keyword:\n\n"
                    'def set_age(age):\n'
                    '    if age < 0:\n'
                    '        raise ValueError("Age cannot be negative.")\n'
                    '    if age > 150:\n'
                    '        raise ValueError("Age is not realistic.")\n'
                    '    return age\n\n'
                    'try:\n'
                    '    set_age(-5)\n'
                    'except ValueError as e:\n'
                    '    print(f"Invalid age: {e}")\n\n'
                    "The as e syntax captures the exception object and lets you access its message. This is useful when you want to display what went wrong without writing a separate message in the except block.\n\n"
                    "When you write a function, you're defining a contract — here's what I expect to receive, and here's what I'll give back. Raising exceptions is how you enforce that contract. If someone calls your function with values that make no sense, raising an error immediately is far better than letting the function quietly produce a wrong result that causes problems somewhere else in the program later:\n\n"
                    'def calculate_tip(bill_amount, tip_percent):\n'
                    '    if bill_amount < 0:\n'
                    '        raise ValueError("Bill amount cannot be negative.")\n'
                    '    if not 0 <= tip_percent <= 100:\n'
                    '        raise ValueError("Tip percentage must be between 0 and 100.")\n'
                    '    tip = bill_amount * (tip_percent / 100)\n'
                    '    return tip\n\n'
                    "This is exactly the kind of defensive programming that separates reliable software from brittle software."
                ),
            },
            {
                'title': 'Mini Project: Number Guessing Game with Error Handling',
                'body': (
                    "In Section 4 we built a number guessing game. It works great when the user enters a valid number, but try typing \"hello\" and it crashes immediately. Let's fix that.\n\n"
                    "The challenge: update the guessing game so it keeps asking for a guess until the user enters a valid whole number, tells the user clearly when their input is invalid, still tells them if their guess is too high, too low, or correct, and lets them play again after each round without restarting the program.\n\n"
                    'Solution:\n\n'
                    '# Number Guessing Game - with Error Handling\n'
                    'import random\n\n'
                    'def get_valid_guess():\n'
                    '    while True:\n'
                    '        try:\n'
                    '            guess = int(input("Enter your guess (1-20): "))\n'
                    '            if guess < 1 or guess > 20:\n'
                    '                print("Please enter a number between 1 and 20.")\n'
                    '            else:\n'
                    '                return guess\n'
                    '        except ValueError:\n'
                    '            print("That\'s not a valid number. Please enter a whole number between 1 and 20.")\n\n'
                    'def play_game():\n'
                    '    secret_number = random.randint(1, 20)\n'
                    '    while True:\n'
                    '        guess = get_valid_guess()\n'
                    '        if guess == secret_number:\n'
                    '            print(f"That\'s it! The number was {secret_number}. Well done!")\n'
                    '            return\n'
                    '        elif guess < secret_number:\n'
                    '            print("Too low! Try again.")\n'
                    '        else:\n'
                    '            print("Too high! Try again.")\n\n'
                    'def ask_play_again():\n'
                    '    while True:\n'
                    '        answer = input("\\nWould you like to play again? (yes/no): ").lower()\n'
                    '        if answer == "yes":\n'
                    '            return True\n'
                    '        elif answer == "no":\n'
                    '            return False\n'
                    '        else:\n'
                    '            print("Please type \'yes\' or \'no\'.")\n\n'
                    '# Main program\n'
                    'print("Welcome to the Number Guessing Game!")\n'
                    'print("I\'ll think of a number between 1 and 20.")\n\n'
                    'while True:\n'
                    '    play_game()\n'
                    '    if not ask_play_again():\n'
                    '        break\n\n'
                    'print("\\nThanks for playing. Goodbye!")\n\n'
                    "A few things worth noting: get_valid_guess() is a dedicated function whose only job is collecting a valid guess, looping with while True and only exiting via return when the input passes both checks — except ValueError catches non-numeric input, and the range check catches numbers outside 1-20. play_game() contains the core game logic and now allows multiple guesses per round, exiting cleanly with return when the user guesses correctly. ask_play_again() keeps asking until the user types exactly \"yes\" or \"no,\" with .lower() ensuring \"Yes,\" \"YES,\" and \"yes\" are all treated the same. Notice how the main program is now just a few lines — the complexity is hidden inside focused, well-named functions. That's exactly what good function design looks like: each piece has one job, and the main program just orchestrates them."
                ),
            },
        ],
    },
    {
        'title': 'Section 8: Working with Files',
        'goal': 'Read and write data that persists between runs.',
        'lectures': [
            {
                'title': 'Opening and Closing Files',
                'body': (
                    "Every program we've built so far has had one significant limitation: when you close it, everything is gone. The shopping list, the contacts, the guesses — none of it survives between runs. The data only exists in memory while the program is running.\n\n"
                    "In the real world, data needs to persist. A to-do list that forgets all your tasks the moment you close it isn't very useful. To make data stick around, we need to save it somewhere permanent, and the simplest place to start is a file.\n\n"
                    "Python makes working with files straightforward. The built-in open() function is the gateway to any file on your system. It takes two main arguments: the file path and the mode, which tells Python what you intend to do with the file.\n\n"
                    'file = open("tasks.txt", "r")\n\n'
                    "The mode is a string that controls how the file is opened. \"r\" is read mode — opens the file for reading; the file must already exist or Python raises a FileNotFoundError. \"w\" is write mode — opens the file for writing; if the file already exists it is completely overwritten, and if it doesn't exist Python creates it automatically. \"a\" is append mode — opens the file for writing but adds new content to the end rather than overwriting, creating the file if it doesn't exist. \"x\" is create mode — creates a new file and raises an error if the file already exists.\n\n"
                    "Once you're done with a file, you should close it. An open file uses system resources and in some cases can prevent other programs from accessing it while it's open. Closing is done with .close():\n\n"
                    'file = open("tasks.txt", "r")\n'
                    '# ...do something with the file\n'
                    'file.close()\n\n'
                    "This works, but it has a problem. If an error occurs between open() and close(), the close() line never runs and the file stays open. This is exactly the kind of situation Python's with statement was designed to solve — we'll cover it a little later in this section. For now, let's focus on reading and writing."
                ),
            },
            {
                'title': 'Reading a File',
                'body': (
                    "Let's start by reading from a file. Suppose you have a file called sample.txt in your project folder with a few lines of text in it:\n\n"
                    'Apples\n'
                    'Bread\n'
                    'Milk\n'
                    'Eggs\n\n'
                    "The .read() method reads the entire contents of a file as a single string:\n\n"
                    'file = open("sample.txt", "r")\n'
                    'content = file.read()\n'
                    'file.close()\n'
                    'print(content)\n\n'
                    "The .readlines() method reads the file and returns each line as an item in a list:\n\n"
                    'file = open("sample.txt", "r")\n'
                    'lines = file.readlines()\n'
                    'file.close()\n'
                    'print(lines)\n'
                    "# ['Apples\\n', 'Bread\\n', 'Milk\\n', 'Eggs\\n']\n\n"
                    "Notice the \\n at the end of each item — that's the newline character that marks the end of each line in the file. You'll often want to strip these when working with the data:\n\n"
                    'for line in lines:\n'
                    '    print(line.strip())\n\n'
                    ".strip() removes whitespace and newline characters from both ends of a string, leaving you with the clean text. The .readline() method reads a single line each time it's called, and Python keeps track of where it is in the file so each call picks up where the last one left off:\n\n"
                    'file = open("sample.txt", "r")\n'
                    'print(file.readline())   # Apples\n'
                    'print(file.readline())   # Bread\n'
                    'file.close()\n\n'
                    "The most memory-efficient way to read a file line by line is to loop through it directly — Python reads one line at a time without loading the entire file into memory:\n\n"
                    'file = open("sample.txt", "r")\n'
                    'for line in file:\n'
                    '    print(line.strip())\n'
                    'file.close()\n\n'
                    "For small files it doesn't make much difference, but for large files this approach is significantly more efficient."
                ),
            },
            {
                'title': 'Writing to a File',
                'body': (
                    "Writing to a file uses write mode \"w\". The .write() method takes a string and writes it to the file:\n\n"
                    'file = open("output.txt", "w")\n'
                    'file.write("Hello, World!\\n")\n'
                    'file.write("This is my first file.\\n")\n'
                    'file.close()\n\n'
                    "Notice we added \\n at the end of each string. Unlike print(), .write() doesn't add a newline automatically — if you leave it out, everything runs together on one line.\n\n"
                    "This is the most important thing to understand about write mode: every time you open a file with \"w\", the existing contents are completely erased before anything is written. Even opening a file in write mode and immediately closing it without writing anything will result in an empty file:\n\n"
                    '# First run - writes two lines\n'
                    'file = open("output.txt", "w")\n'
                    'file.write("Line 1\\n")\n'
                    'file.write("Line 2\\n")\n'
                    'file.close()\n\n'
                    '# Second run - completely replaces the contents\n'
                    'file = open("output.txt", "w")\n'
                    'file.write("Line 3\\n")\n'
                    'file.close()\n\n'
                    "After the second run, output.txt contains only Line 3. Lines 1 and 2 are gone. Keep this in mind — write mode is for when you want to replace the entire contents of a file.\n\n"
                    "You can write a list of strings at once using .writelines(). Note that it does not add newlines automatically — each string in the list needs to include its own \\n:\n\n"
                    'tasks = ["Buy groceries\\n", "Walk the dog\\n", "Call the dentist\\n"]\n'
                    'file = open("tasks.txt", "w")\n'
                    'file.writelines(tasks)\n'
                    'file.close()'
                ),
            },
            {
                'title': 'Appending to a File',
                'body': (
                    "Append mode \"a\" is like write mode, except instead of overwriting the file it adds new content to the end. Existing content is preserved:\n\n"
                    'file = open("tasks.txt", "a")\n'
                    'file.write("Read a book\\n")\n'
                    'file.close()\n\n'
                    "If tasks.txt previously contained three tasks, it now contains four. The new line is added at the end and nothing else is touched. This is the mode you'll use when you want to add to a file over time — a log file, a growing list, a record of events — rather than replacing everything each time.\n\n"
                    '# Write mode - starts fresh every time\n'
                    'file = open("log.txt", "w")\n'
                    'file.write("Session started\\n")\n'
                    'file.close()\n\n'
                    '# Append mode - adds to what\'s already there\n'
                    'file = open("log.txt", "a")\n'
                    'file.write("User logged in\\n")\n'
                    'file.close()\n\n'
                    'file = open("log.txt", "a")\n'
                    'file.write("User logged out\\n")\n'
                    'file.close()\n\n'
                    'Result in log.txt:\n'
                    'Session started\n'
                    'User logged in\n'
                    'User logged out\n\n'
                    "If the second and third calls had used \"w\" instead of \"a\", the file would only contain User logged out."
                ),
            },
            {
                'title': 'Working with File Paths',
                'body': (
                    "When you open a file by name alone, open(\"tasks.txt\"), Python looks for it in the current working directory, which is the folder your script is running from. For simple projects where your script and data files live in the same folder, this works perfectly. But as projects grow you'll often need to work with files in different locations.\n\n"
                    "An absolute path specifies the exact location of a file from the root of the file system:\n\n"
                    '# Windows\n'
                    'file = open("C:/Users/yourname/Documents/tasks.txt", "r")\n'
                    '# Mac/Linux\n'
                    'file = open("/Users/yourname/Documents/tasks.txt", "r")\n\n'
                    "Absolute paths always work regardless of where your script is running from, but they're not portable — if you share your code with someone else or move it to a different machine, the path breaks.\n\n"
                    "A relative path specifies the location of a file relative to where your script is. If your script and your file are in the same folder, just the filename works:\n\n"
                    'file = open("tasks.txt", "r")\n\n'
                    "You can also navigate into subfolders:\n\n"
                    'file = open("data/tasks.txt", "r")      # file is in a subfolder called data\n'
                    'file = open("../tasks.txt", "r")        # file is in the parent folder\n\n'
                    "Python's built-in os module provides tools for working with file paths in a way that works correctly on both Windows and Mac/Linux, since the two systems use different path separators (\\ vs /):\n\n"
                    'import os\n'
                    '# Get the directory where the script is located\n'
                    'script_dir = os.path.dirname(__file__)\n'
                    '# Build a path to a file in the same directory\n'
                    'file_path = os.path.join(script_dir, "tasks.txt")\n'
                    'file = open(file_path, "r")\n\n'
                    "os.path.join() builds the path using the correct separator for the operating system automatically. This is the safest approach for any project that might be shared or moved.\n\n"
                    "Before opening a file for reading it's good practice to check whether it actually exists first, otherwise Python will raise a FileNotFoundError:\n\n"
                    'import os\n'
                    'if os.path.exists("tasks.txt"):\n'
                    '    file = open("tasks.txt", "r")\n'
                    '    content = file.read()\n'
                    '    file.close()\n'
                    '    print(content)\n'
                    'else:\n'
                    '    print("File not found.")\n\n'
                    "We'll use this pattern in this section's mini project to handle the case where the tasks file doesn't exist yet on the first run."
                ),
            },
            {
                'title': 'Introduction to with Statements',
                'body': (
                    "Earlier we mentioned that opening a file and then hitting an error before closing it leaves the file open. The with statement solves this elegantly. It's Python's way of managing resources that need to be cleaned up, and files are the most common use case.\n\n"
                    'with open("tasks.txt", "r") as file:\n'
                    '    content = file.read()\n'
                    '    print(content)\n\n'
                    "The as file part gives the opened file a name to work with inside the block. When the with block ends, whether normally or because of an exception, Python automatically closes the file. You don't have to call .close() at all. This is the modern, preferred way to work with files in Python.\n\n"
                    "Reading with with:\n\n"
                    'with open("sample.txt", "r") as file:\n'
                    '    for line in file:\n'
                    '        print(line.strip())\n\n'
                    "Writing with with:\n\n"
                    'tasks = ["Buy groceries", "Walk the dog", "Call the dentist"]\n'
                    'with open("tasks.txt", "w") as file:\n'
                    '    for task in tasks:\n'
                    '        file.write(task + "\\n")\n\n'
                    "Appending with with:\n\n"
                    'with open("tasks.txt", "a") as file:\n'
                    '    file.write("Read a book\\n")\n\n'
                    "Clean, safe, and concise. The with statement is one of those Python features that once you start using it, you'll never go back."
                ),
            },
            {
                'title': 'Mini Project: Persistent To-Do List',
                'body': (
                    "You've learned how to open, read, write, and append files, work with file paths, and use with statements. Now let's build a to-do list that actually remembers your tasks between runs.\n\n"
                    "The challenge: save tasks to a file called tasks.txt so they persist when the program closes, load existing tasks from the file when the program starts, show a menu with Add, View, Remove, and Quit options, save the updated list after every change, and handle the case where tasks.txt doesn't exist yet on the first run.\n\n"
                    'Solution:\n\n'
                    '# Persistent To-Do List\n'
                    'import os\n\n'
                    'FILENAME = "tasks.txt"\n\n'
                    'def load_tasks():\n'
                    '    if not os.path.exists(FILENAME):\n'
                    '        return []\n'
                    '    with open(FILENAME, "r") as file:\n'
                    '        return [line.strip() for line in file if line.strip()]\n\n'
                    'def save_tasks(tasks):\n'
                    '    with open(FILENAME, "w") as file:\n'
                    '        for task in tasks:\n'
                    '            file.write(task + "\\n")\n\n'
                    'def display_tasks(tasks):\n'
                    '    if len(tasks) == 0:\n'
                    '        print("Your to-do list is empty.")\n'
                    '    else:\n'
                    '        print("\\nYour To-Do List:")\n'
                    '        for index, task in enumerate(tasks):\n'
                    '            print(f"  {index + 1}. {task}")\n\n'
                    'def add_task(tasks):\n'
                    '    task = input("Enter the task: ")\n'
                    '    tasks.append(task)\n'
                    '    save_tasks(tasks)\n'
                    '    print(f"\'{task}\' has been added to your list.")\n\n'
                    'def remove_task(tasks):\n'
                    '    if len(tasks) == 0:\n'
                    '        print("Your list is empty - nothing to remove.")\n'
                    '        return\n'
                    '    display_tasks(tasks)\n'
                    '    try:\n'
                    '        number = int(input("\\nEnter the number of the task to remove: "))\n'
                    '        if 1 <= number <= len(tasks):\n'
                    '            removed = tasks.pop(number - 1)\n'
                    '            save_tasks(tasks)\n'
                    '            print(f"\'{removed}\' has been removed from your list.")\n'
                    '        else:\n'
                    '            print("Invalid number. Please choose a number from the list.")\n'
                    '    except ValueError:\n'
                    '        print("Please enter a valid number.")\n\n'
                    '# Load existing tasks on startup\n'
                    'tasks = load_tasks()\n'
                    'print("Welcome to your To-Do List!")\n\n'
                    'while True:\n'
                    '    print("\\n--- To-Do List ---")\n'
                    '    print("1. Add a task")\n'
                    '    print("2. View tasks")\n'
                    '    print("3. Remove a task")\n'
                    '    print("4. Quit")\n'
                    '    choice = input("\\nChoose an option (1-4): ")\n\n'
                    '    if choice == "1":\n'
                    '        add_task(tasks)\n'
                    '    elif choice == "2":\n'
                    '        display_tasks(tasks)\n'
                    '    elif choice == "3":\n'
                    '        remove_task(tasks)\n'
                    '    elif choice == "4":\n'
                    '        print("Goodbye! Your tasks have been saved.")\n'
                    '        break\n'
                    '    else:\n'
                    '        print("Invalid option. Please choose 1, 2, 3, or 4.")\n\n'
                    "A few things worth noting: FILENAME = \"tasks.txt\" stores the filename as a constant at the top of the file, so if you ever want to rename it you only change it in one place. load_tasks() uses os.path.exists() to check whether the file exists before trying to open it — on the very first run the file won't exist yet, so without this check the program would crash with a FileNotFoundError; if the file doesn't exist it returns an empty list and the program starts fresh. [line.strip() for line in file if line.strip()] is a list comprehension, a compact way to build a list in a single line — it reads every line from the file, strips whitespace and newlines from each one, and skips any blank lines; we'll cover list comprehensions more formally in Section 9. save_tasks(tasks) is called immediately after every change, rewriting the entire file from scratch each time using write mode — for a small to-do list this is perfectly fine, and it keeps the save logic simple and reliable. tasks.pop(number - 1) removes the task at the chosen position, subtracting 1 because the user sees a list starting from 1 but Python's list indices start at 0. Functions doing one job each — load_tasks() loads, save_tasks() saves, display_tasks() displays, add_task() adds, remove_task() removes — is clean, organized, well-structured Python, exactly the kind of code that scales well as programs grow."
                ),
            },
        ],
    },
    {
        'title': 'Section 9: Modules & Libraries',
        'goal': 'Extend Python with built-in and external tools.',
        'lectures': [
            {
                'title': 'What is a Module?',
                'body': (
                    "Throughout this course we've been writing all of our code in a single file. That works fine for small programs, but imagine building something much larger — a program with hundreds or thousands of lines covering dozens of different features. Keeping all of that in one file would be overwhelming to navigate, impossible to maintain, and impossible to share with other developers.\n\n"
                    "Python solves this with modules. A module is simply a Python file containing code — functions, variables, classes — that can be imported and used in other Python files. Instead of writing everything from scratch in one place, you organize related code into separate files and pull in what you need when you need it.\n\n"
                    "You've already been using modules. Back in Section 3 we wrote import random at the top of the guessing game. That one line gave us access to an entire collection of functions for generating random numbers — functions written by someone else, tested thoroughly, and made available for any Python program to use.\n\n"
                    "There are three categories of modules you'll work with. Built-in modules come with Python and are available immediately, no installation needed — random, math, os, and datetime are all built in; you just import them and start using them. Third-party modules are packages written by other developers and published to the Python Package Index (PyPI) — they don't come with Python but can be installed with a single command using pip; libraries like requests for making web requests and django for building web applications fall into this category. Your own modules are files you write yourself — any .py file you create can be imported into another file, and this is how larger Python projects are organized: the code is spread across multiple files, each focused on a specific responsibility, importing from each other as needed.\n\n"
                    "Let's explore each of these, starting with Python's most useful built-in modules."
                ),
            },
            {
                'title': 'Importing Built-in Modules',
                'body': (
                    "Python ships with a large collection of built-in modules covering everything from mathematics to file handling to working with dates. You bring a module into your program using the import statement, which always goes at the very top of your file. Let's walk through four of the most useful ones.\n\n"
                    "The random module provides tools for generating random numbers and making random selections. We used it briefly in Section 3 — now let's look at what else it can do:\n\n"
                    'import random\n\n'
                    '# Random integer between 1 and 10 inclusive\n'
                    'print(random.randint(1, 10))\n'
                    '# Random float between 0 and 1\n'
                    'print(random.random())\n'
                    '# Pick a random item from a list\n'
                    'colors = ["red", "green", "blue", "yellow"]\n'
                    'print(random.choice(colors))\n'
                    '# Pick multiple random items from a list (no duplicates)\n'
                    'print(random.sample(colors, 2))\n'
                    '# Shuffle a list in place\n'
                    'random.shuffle(colors)\n'
                    'print(colors)\n\n'
                    "random.choice() and random.sample() are particularly useful any time you need to select randomly from a collection — quotes, questions, colors, names. We'll use random.choice() in this section's mini project.\n\n"
                    "The math module provides mathematical functions and constants beyond what Python's basic operators offer:\n\n"
                    'import math\n\n'
                    'print(math.pi)           # 3.141592653589793\n'
                    'print(math.sqrt(144))    # 12.0 - square root\n'
                    'print(math.ceil(4.3))    # 5 - round up to nearest integer\n'
                    'print(math.floor(4.9))   # 4 - round down to nearest integer\n'
                    'print(math.pow(2, 8))    # 256.0 - 2 to the power of 8\n\n'
                    "math.ceil() and math.floor() are particularly handy in everyday programming — for example, working out how many pages a list of results needs, or rounding prices in a specific direction.\n\n"
                    "The datetime module is your toolkit for working with dates and times. It's one of the most commonly used modules in real-world Python:\n\n"
                    'from datetime import date, timedelta\n\n'
                    '# Just today\'s date\n'
                    'today = date.today()\n'
                    'print(today)                          # 2026-07-13\n'
                    '# Formatting dates as readable strings\n'
                    'print(today.strftime("%B %d, %Y"))    # July 13, 2026\n'
                    'print(today.strftime("%A"))           # Monday\n'
                    '# Accessing individual components\n'
                    'print(today.year)     # 2026\n'
                    'print(today.month)    # 7\n'
                    '# Date arithmetic with timedelta\n'
                    'tomorrow = today + timedelta(days=1)\n'
                    'last_week = today - timedelta(weeks=1)\n\n'
                    "strftime() — short for \"string format time\" — converts a date object into a human-readable string. Format codes like %B for full month name and %A for full day name are standard across most programming languages, so learning them here will serve you well beyond Python. We'll use datetime in this section's mini project to display today's date alongside a motivational quote.\n\n"
                    "We already used os in Section 8 for file path operations. Let's look at more of what it offers:\n\n"
                    'import os\n\n'
                    '# Get current working directory\n'
                    'print(os.getcwd())\n'
                    '# List files and folders in a directory\n'
                    'print(os.listdir("."))\n'
                    '# Get just the filename from a full path\n'
                    'print(os.path.basename("/Users/mike/projects/tasks.txt"))   # tasks.txt\n'
                    '# Create a new directory\n'
                    'os.makedirs("new_folder", exist_ok=True)\n\n'
                    "os.makedirs() with exist_ok=True creates a folder without throwing an error if it already exists — a small but useful detail.\n\n"
                    "Instead of importing an entire module you can import just the parts you need using from ... import:\n\n"
                    'from math import sqrt, pi\n'
                    'from datetime import date\n\n'
                    'print(sqrt(81))     # 9.0\n'
                    'print(pi)           # 3.141592653589793\n'
                    'print(date.today())\n\n'
                    "This means you can use sqrt() directly instead of math.sqrt(). It keeps your code cleaner when you only need a few specific things from a module. You can also give a module or import a shorter nickname using as:\n\n"
                    'import datetime as dt\n'
                    'import random as rnd\n\n'
                    'print(dt.date.today())\n'
                    'print(rnd.randint(1, 10))\n\n'
                    "This is common with modules that have long names. In the data science world you'll often see import numpy as np and import pandas as pd — industry-standard aliases that everyone recognizes."
                ),
            },
            {
                'title': 'Installing External Packages with pip',
                'body': (
                    "Built-in modules are powerful, but Python's real strength comes from its enormous ecosystem of third-party packages. Whatever you want to build, there's almost certainly a package that either does it for you or makes it significantly easier.\n\n"
                    "All of these packages live on the Python Package Index, known as PyPI, at pypi.org, with hundreds of thousands of packages available covering everything from web development to machine learning to working with spreadsheets. You install packages from PyPI using pip, Python's package installer — it comes bundled with Python so you already have it.\n\n"
                    "To install a package, open your terminal and run:\n\n"
                    'pip install package-name\n\n'
                    "For example, to install the popular requests library for making HTTP requests:\n\n"
                    'pip install requests\n\n'
                    "pip downloads the package from PyPI and installs it into your Python environment. Once installed, you can import it just like a built-in module:\n\n"
                    'import requests\n\n'
                    'response = requests.get("https://api.github.com")\n'
                    'print(response.status_code)   # 200\n\n'
                    "Sometimes you need a specific version of a package for compatibility with other packages or to match a tutorial:\n\n"
                    'pip install django==5.0.0\n\n'
                    "To see every package currently installed in your environment, run pip list. To remove one, run pip uninstall package-name.\n\n"
                    "When you're working on a project you share with others, or deploy to a server, they need to know which packages to install and which versions you used. The convention is to list them in a file called requirements.txt:\n\n"
                    'django==5.0.0\n'
                    'requests==2.31.0\n'
                    'pillow==10.0.0\n\n'
                    "You can create the requirements.txt file right from the terminal with pip freeze > requirements.txt, which creates or updates the file with all packages installed in the project environment. Anyone who clones your project can then install everything at once with:\n\n"
                    'pip install -r requirements.txt\n\n'
                    "This is standard practice in professional Python development. You'll see it in almost every real-world project you encounter."
                ),
            },
            {
                'title': 'Introduction to pip and Virtual Environments',
                'body': (
                    "You might be wondering: when you install a package with pip, where does it actually go? By default it goes into your system-wide Python installation, which means every Python project on your computer shares the same pool of packages.\n\n"
                    "This creates a problem. Imagine you have two projects — one that needs Django version 4 and another that needs Django version 6. They can't both be installed system-wide at the same time. One will break the other. This is exactly the problem virtual environments solve.\n\n"
                    "A virtual environment is an isolated copy of Python with its own separate set of installed packages. When it's active, any package you install with pip goes into that environment only, completely separate from your system Python and from every other project's environment. Each project ends up with exactly the packages it needs at exactly the versions it needs, with no conflicts.\n\n"
                    "After creating a workspace folder and opening it in your code editor, create a virtual environment:\n\n"
                    '# Windows\n'
                    'python -m venv .venv\n'
                    '# Mac/Linux\n'
                    'python3 -m venv .venv\n\n'
                    "Then activate it:\n\n"
                    '# Windows\n'
                    '.venv\\Scripts\\activate\n'
                    '# Mac/Linux\n'
                    'source .venv/bin/activate\n\n'
                    "Once activated you'll see (.venv) in your terminal prompt before the folder path. Any pip install from this point installs into the environment, not your system. When you're done working, just type deactivate.\n\n"
                    "The golden rule: always create and activate a virtual environment before starting a new Python project, and always install packages into it rather than system-wide. This habit will save you from dependency conflicts and make your projects portable and reproducible. It's one of those professional practices that separates tidy, maintainable projects from messy ones."
                ),
            },
            {
                'title': 'Mini Project: Daily Motivational Quote Generator',
                'body': (
                    "You've learned what modules are, how to use built-in modules, how to install external packages with pip, and how virtual environments keep your projects clean and organized. Now let's put the built-in modules to work in a fun, practical project.\n\n"
                    "The challenge: store a collection of at least ten motivational quotes, pick a random one each time the program runs, display today's date in a clean, readable format alongside the quote, and let the user request another quote without repeats until every quote has been shown, then reshuffle.\n\n"
                    'Solution:\n\n'
                    '# Daily Motivational Quote Generator\n'
                    'import random\n'
                    'from datetime import date\n\n'
                    'quotes = [\n'
                    '    {"quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},\n'
                    '    {"quote": "It always seems impossible until it\'s done.", "author": "Nelson Mandela"},\n'
                    '    {"quote": "Don\'t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},\n'
                    '    {"quote": "Believe you can and you\'re halfway there.", "author": "Theodore Roosevelt"},\n'
                    '    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},\n'
                    '    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},\n'
                    '    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},\n'
                    '    {"quote": "Life is what happens when you\'re busy making other plans.", "author": "John Lennon"},\n'
                    '    {"quote": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},\n'
                    '    {"quote": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},\n'
                    ']\n\n'
                    'def get_todays_date():\n'
                    '    today = date.today()\n'
                    '    return today.strftime("%A, %B %d, %Y")\n\n'
                    'def display_quote(quote_data, number, total):\n'
                    '    print("\\n" + "=" * 50)\n'
                    '    print(f"  {get_todays_date()}")\n'
                    '    print(f"  Quote {number} of {total}")\n'
                    '    print("=" * 50)\n'
                    '    print(f"\\n  \\"{quote_data[\'quote\']}\\"")\n'
                    '    print(f"\\n  - {quote_data[\'author\']}")\n'
                    '    print("\\n" + "=" * 50)\n\n'
                    'def run_generator():\n'
                    '    total = len(quotes)\n'
                    '    remaining = quotes.copy()\n'
                    '    random.shuffle(remaining)\n'
                    '    quote_number = 1\n\n'
                    '    print("\\nWelcome to your Daily Motivational Quote Generator!")\n'
                    '    while True:\n'
                    '        if len(remaining) == 0:\n'
                    '            print("\\nYou\'ve seen all the quotes! Shuffling and starting over.")\n'
                    '            remaining = quotes.copy()\n'
                    '            random.shuffle(remaining)\n'
                    '            quote_number = 1\n\n'
                    '        current_quote = remaining.pop()\n'
                    '        display_quote(current_quote, quote_number, total)\n'
                    '        quote_number += 1\n\n'
                    '        print("\\nOptions:")\n'
                    '        print("  1. Get another quote")\n'
                    '        print("  2. Quit")\n'
                    '        choice = input("\\nChoose an option (1/2): ").strip()\n\n'
                    '        if choice == "2":\n'
                    '            print("\\nKeep going - you\'ve got this! Goodbye.\\n")\n'
                    '            break\n'
                    '        elif choice != "1":\n'
                    '            print("Invalid option - showing next quote anyway.")\n\n'
                    'run_generator()\n\n'
                    "A few things worth noting: import random and from datetime import date bring in two built-in modules working together — random handles the shuffling and selection, datetime provides today's date, and neither required installation since they came with Python. quotes is stored as a list of dictionaries, applying the nested data structure pattern from Section 5 to a real use case, keeping the quote text and author name cleanly paired together. remaining = quotes.copy() creates a copy of the quotes list rather than working with the original — this matters because if we shuffled and popped from quotes directly, the original list would be destroyed, so using a copy means the original is always intact and ready to be reused once the user has seen everything. remaining.pop() removes and returns the last item from the list on each pass, combined with the shuffle giving us a clean way to serve quotes without repeating. quote_number += 1 is shorthand for quote_number = quote_number + 1 — the += operator adds to a variable in place and works the same way for -=, *=, and /=, a pattern you'll use constantly."
                ),
            },
        ],
    },
    {
        'title': 'Section 10: Introduction to Classes & Objects',
        'goal': 'Understand object-oriented programming basics.',
        'lectures': [
            {
                'title': 'What is a Class?',
                'body': (
                    "Throughout this course we've worked with Python's built-in data types: strings, integers, floats, lists, Booleans, tuples, and dictionaries. These are great for storing simple pieces of data, but as programs grow more complex, you start to need something more powerful — a way to bundle related data and the actions that work on that data together into a single, organized unit.\n\n"
                    "That's exactly what a class does. A class is a blueprint for creating objects. It defines what data an object should hold and what actions it should be able to perform. Once the blueprint exists, you can create as many objects from it as you need, each one its own independent copy with its own data.\n\n"
                    "You've actually been using classes this entire course without realizing it. Every time you create a string, a list, or a dictionary, Python is creating an object from a built-in class behind the scenes. When you call \"hello\".upper() you're calling a method on a string object. When you call my_list.append(\"item\") you're calling a method on a list object. The data and the actions that work on it are bundled together — that's object-oriented programming.\n\n"
                    "Think of a class like a house blueprint. The blueprint itself isn't a house, it's the plan for one. From that single plan you can build an infinite number of houses. Yet despite sharing the same blueprint, each house can have unique details that set it apart from the rest — the color of the siding, the shade of the roof, the style of the front door.\n\n"
                    "In programming, a class works the same way. You define it once, and from it you can create as many individual instances as you need, each one sharing the same structure but carrying its own unique values. A class is the plan. An instance is the thing built from the plan."
                ),
            },
            {
                'title': 'Attributes and Methods',
                'body': (
                    "A class bundles together two things: attributes and methods.\n\n"
                    "Attributes are the data — the characteristics that describe an object. For a house they might be the siding color, roof color, and number of bedrooms. For a task they might be the title, whether it's completed, and when it was created.\n\n"
                    "Methods are the actions — the things an object can do. For a house that might be open_door() or turn_on_lights(). For a task it might be complete() or display().\n\n"
                    "Together, attributes and methods describe everything about what an object is and what it can do. Here's a simple example to make this concrete before we go deeper:\n\n"
                    'class Dog:\n'
                    '    # Attributes describe what a dog IS\n'
                    '    name = "Buddy"\n'
                    '    breed = "Labrador"\n\n'
                    '    # Methods describe what a dog DOES\n'
                    '    def bark(self):\n'
                    '        print(f"{self.name} says: Woof!")\n\n'
                    "name and breed are attributes. bark() is a method. Notice the self parameter in bark() — we'll explain exactly what that means in the next lecture, but for now just know that every method in a class takes self as its first parameter."
                ),
            },
            {
                'title': '__init__',
                'body': (
                    "The Dog example from the last lecture has a problem. Every Dog object would have the name \"Buddy\" and be a Labrador, because we hardcoded those values directly into the class. That's not useful — we want each instance to have its own unique data. This is where __init__ comes in.\n\n"
                    "__init__ is a special method called the initializer, sometimes called the constructor. It runs automatically every time you create a new instance of the class, and it's where you set the initial values of the object's attributes. The double underscores on either side of init are Python's way of marking it as a special built-in method — you'll sometimes hear these called dunder methods, short for \"double underscore.\"\n\n"
                    'class Dog:\n'
                    '    def __init__(self, name, breed):\n'
                    '        self.name = name\n'
                    '        self.breed = breed\n\n'
                    '    def bark(self):\n'
                    '        print(f"{self.name} says: Woof!")\n\n'
                    "Let's break down exactly what's happening here. def __init__(self, name, breed) defines the initializer with three parameters — self refers to the specific instance being created, and name and breed are the values we'll pass in when creating a new dog. self.name = name takes the name argument and stores it as an attribute on the instance — self.name is the instance's own copy of that value, separate from any other instance. self.breed = breed does the same for breed.\n\n"
                    "Think of self as the object saying \"this is mine.\" self.name means \"my name\" — not just any variable called name, but the name that belongs to this particular instance."
                ),
            },
            {
                'title': 'Creating Instances',
                'body': (
                    "With the class defined, creating an instance is straightforward. You call the class like a function and pass in the arguments that __init__ expects:\n\n"
                    'dog1 = Dog("Buddy", "Labrador")\n'
                    'dog2 = Dog("Luna", "Poodle")\n'
                    'dog3 = Dog("Max", "Beagle")\n\n'
                    "Each one is a completely independent object with its own data. They all came from the same blueprint but they're not connected to each other in any way. You access an instance's attributes using dot notation:\n\n"
                    'print(dog1.name)    # Buddy\n'
                    'print(dog2.breed)   # Poodle\n\n'
                    "You call methods the same way:\n\n"
                    'dog1.bark()   # Buddy says: Woof!\n'
                    'dog2.bark()   # Luna says: Woof!\n\n'
                    "Same method, different results, because each instance has its own self.name. The method runs in the context of whichever object called it. You can also update an instance's attributes directly:\n\n"
                    'dog1.name = "Charlie"\n'
                    'print(dog1.name)   # Charlie\n'
                    'print(dog2.name)   # Luna - unchanged\n\n'
                    "Changing dog1's name has no effect on dog2. Each instance is completely independent.\n\n"
                    "Let's build something a little closer to what we'll use in the mini project — a BankAccount class that demonstrates attributes and methods working together:\n\n"
                    'class BankAccount:\n'
                    '    def __init__(self, owner, balance=0):\n'
                    '        self.owner = owner\n'
                    '        self.balance = balance\n\n'
                    '    def deposit(self, amount):\n'
                    '        self.balance += amount\n'
                    '        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")\n\n'
                    '    def withdraw(self, amount):\n'
                    '        if amount > self.balance:\n'
                    '            print("Insufficient funds.")\n'
                    '        else:\n'
                    '            self.balance -= amount\n'
                    '            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")\n\n'
                    '    def display(self):\n'
                    '        print(f"Account owner: {self.owner}")\n'
                    '        print(f"Current balance: ${self.balance:.2f}")\n\n'
                    'account1 = BankAccount("Mike", 1000)\n'
                    'account2 = BankAccount("Sarah")\n\n'
                    'account1.deposit(500)\n'
                    'account1.withdraw(200)\n'
                    'account1.display()\n\n'
                    'account2.deposit(250)\n'
                    'account2.display()\n\n'
                    "Each account has its own owner and balance. Methods like deposit() and withdraw() modify self.balance — the balance belonging to whichever account called the method. account1's balance has nothing to do with account2's balance."
                ),
            },
            {
                'title': 'The Blueprint Analogy in Code',
                'body': (
                    "Let's revisit the house blueprint analogy now that we understand the syntax. Looking at it in code makes the connection between classes and instances completely concrete:\n\n"
                    'class House:\n'
                    '    def __init__(self, siding_color, roof_color, bedrooms):\n'
                    '        self.siding_color = siding_color\n'
                    '        self.roof_color = roof_color\n'
                    '        self.bedrooms = bedrooms\n\n'
                    '    def describe(self):\n'
                    '        print(f"A {self.bedrooms}-bedroom house with {self.siding_color} siding and a {self.roof_color} roof.")\n\n'
                    '# One blueprint, four unique houses\n'
                    'house1 = House("red", "dark red", 3)\n'
                    'house2 = House("blue", "slate grey", 4)\n'
                    'house3 = House("green", "brown", 2)\n'
                    'house4 = House("yellow", "terracotta", 3)\n\n'
                    'house1.describe()   # A 3-bedroom house with red siding and a dark red roof.\n'
                    'house2.describe()   # A 4-bedroom house with blue siding and a slate grey roof.\n\n'
                    "House is the blueprint. house1, house2, house3, and house4 are the instances — each built from the same plan but carrying their own unique values. This is the core idea of object-oriented programming, and it's the foundation everything in Django is built on."
                ),
            },
            {
                'title': 'Why Django Uses Classes Everywhere',
                'body': (
                    "Now that you understand classes and instances, a huge amount of Django that might have seemed confusing before is going to start making sense. Let's look at a typical Django Task model:\n\n"
                    'from django.db import models\n\n'
                    'class Task(models.Model):\n'
                    '    title = models.CharField(max_length=200)\n'
                    '    completed = models.BooleanField(default=False)\n'
                    '    created_at = models.DateTimeField(auto_now_add=True)\n\n'
                    '    def __str__(self):\n'
                    '        return self.title\n\n'
                    "You now have the vocabulary to read this clearly. class Task defines a blueprint called Task. (models.Model) means Task inherits from Django's built-in Model class — this is called inheritance, and it means Task gets all the functionality of Model for free and adds its own on top. We haven't covered inheritance formally in this course, but you now understand enough to recognize what's happening. title, completed, and created_at are the attributes — each one describes a piece of data the task holds. def __str__(self) is a method that returns a string representation of the object — Django calls this automatically in the admin panel to display each task by name rather than as a generic object reference.\n\n"
                    "When you save a task in the Django admin panel or through a web form, Django is creating an instance of the Task class — one object with its own title, its own completed status, its own timestamp. Every task in the database is its own independent instance of the same blueprint.\n\n"
                    "That's it. That's what's happening every time you work with a Django model. The same pattern applies to Django views, forms, and URL configurations — classes with attributes and methods, designed to be extended and customized. Now that you understand the foundation, a Django course is going to feel completely different to read and follow."
                ),
            },
            {
                'title': 'Mini Project: Task Class',
                'body': (
                    "You've learned what a class is, how to define attributes and methods, how __init__ works, how to create instances, and why Django uses classes everywhere. For this final mini project we're going to build something that directly mirrors what a Django model looks like under the hood.\n\n"
                    "The challenge: define a Task class with a title, a completed status that defaults to False, and a created_at timestamp set automatically when the task is created. Include a complete() method that marks the task as done, a display() method that prints the task's details, and a __str__ method that returns the task title — just like the Django model. Create at least three task instances, complete one of them, and display all three to show the difference.\n\n"
                    'Solution:\n\n'
                    '# Task Class - A Preview of Django Models\n'
                    'from datetime import datetime\n\n'
                    'class Task:\n'
                    '    def __init__(self, title):\n'
                    '        self.title = title\n'
                    '        self.completed = False\n'
                    '        self.created_at = datetime.now()\n\n'
                    '    def complete(self):\n'
                    '        if self.completed:\n'
                    '            print(f"\'{self.title}\' is already completed.")\n'
                    '        else:\n'
                    '            self.completed = True\n'
                    '            print(f"\'{self.title}\' has been marked as complete.")\n\n'
                    '    def display(self):\n'
                    '        status = "Done" if self.completed else "Pending"\n'
                    '        created = self.created_at.strftime("%B %d, %Y at %I:%M %p")\n'
                    '        print(f"\\n  Task:    {self.title}")\n'
                    '        print(f"  Status:  {status}")\n'
                    '        print(f"  Created: {created}")\n\n'
                    '    def __str__(self):\n'
                    '        return self.title\n\n'
                    '# Create task instances\n'
                    'task1 = Task("Buy groceries")\n'
                    'task2 = Task("Walk the dog")\n'
                    'task3 = Task("Learn Python")\n\n'
                    '# Complete one task\n'
                    'task2.complete()\n\n'
                    '# Display all tasks\n'
                    'print("\\n" + "=" * 40)\n'
                    'print("  YOUR TASKS")\n'
                    'print("=" * 40)\n'
                    'task1.display()\n'
                    'task2.display()\n'
                    'task3.display()\n'
                    'print("\\n" + "=" * 40)\n\n'
                    '# Demonstrate __str__\n'
                    'print(f"\\nTask names: {task1}, {task2}, {task3}")\n\n'
                    "A few things worth noting: def __init__(self, title) takes only title as an argument — completed and created_at are set automatically inside __init__, just like Django's BooleanField(default=False) and DateTimeField(auto_now_add=True). The user creating a task only needs to provide a title, everything else is handled by the class itself. def complete(self) is a method that modifies the instance's own data using self.completed = True — calling task2.complete() only changes task2's completed status, and task1 and task3 are completely unaffected, which is the core value of instances. def __str__(self) returns self.title as a string representation of the object — when you pass a Task instance to print() or use it in an f-string, Python calls __str__ automatically, identical to the __str__ method in the Django Task model, and it's why tasks display by name in the admin panel rather than as something like <Task object (1)>.\n\n"
                    "Take a moment to compare this pure Python Task class with the Django Task model from the previous lecture. The structure is almost identical — both define title, completed, and created_at, and both have a __str__ method that returns the title. The difference is that Django's version inherits from models.Model, which gives it superpowers like saving to a database, being queried, and appearing in the admin panel. But the underlying concept — a class with attributes and a __str__ method — is exactly what you just built. You didn't just write a mini project. You wrote the foundation of a Django model in pure Python. That's how far you've come."
                ),
            },
        ],
    },
    {
        'title': 'Closing',
        'goal': 'Wrap up the course and plan your next steps.',
        'lectures': [
            {
                'title': 'Course Wrap-Up',
                'body': (
                    "You started this course with a blank editor and no coding experience. Look at where you are now.\n\n"
                    "You know how to store and work with data using variables, strings, numbers, Booleans, lists, dictionaries, and tuples. You know how to make programs respond to users with input and conditional logic. You know how to repeat actions with loops, organize code with functions, handle errors gracefully, save data to files, extend Python with modules, and now model real-world concepts with classes and objects.\n\n"
                    "Every single project you built along the way — the Mad Libs generator, the number guessing game, the shopping list, the contact book, the tip calculator, the to-do list, the quote generator, and finally the Task class — was a real, working Python program. Not exercises. Not fill-in-the-blank worksheets. Real programs that you designed and built yourself.\n\n"
                    "You now have a solid foundation. The next step is yours. Keep building. Keep learning. You've got this."
                ),
            },
        ],
    },
]


def get_module(slug):
    return next((module for module in MODULES if module['slug'] == slug), None)


def get_lesson(slug):
    return next((lesson for lesson in LESSONS if lesson['slug'] == slug), None)
