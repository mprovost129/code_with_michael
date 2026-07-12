SITE_STATS = {
    'followers': '4,500+',
    'lesson_count': 10,
    'challenge_count': 10,
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
    {'title': 'Projects', 'url_name': 'core:projects', 'description': 'Mini builds that combine multiple beginner skills.'},
]

NAV_PAGES_MORE = [
    {'title': 'Tips', 'url_name': 'core:tips', 'description': 'Quick wins and common-mistake fixes from your social content.'},
    {'title': 'Community', 'url_name': 'core:community', 'description': 'Weekly prompts and learner shoutouts connected to your audience.'},
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
        'slug': 'mini-projects',
        'title': 'Mini Projects',
        'duration': '20 min',
        'goal': 'Combine input, conditionals, and f-strings into one small, complete program.',
        'topics': ['combining input and conditionals', 'planning in plain English', 'a simple budget program'],
    },
    {
        'number': 9,
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
        'mini_challenge': 'Add a third print() line that shares your favorite hobby or goal.',
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
        'mini_challenge': 'Create three variables for a hobby, a weekly goal, and the number of practice sessions you want. Print all three values, then update one of them and print it again.',
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
        'mini_challenge': 'Create variables for your name, your favorite hobby, and your current coding goal. Print one polished introduction sentence using an f-string.',
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
        'mini_challenge': 'Create variables for the number of practice sessions you completed this week and the average hours per session. Print the total time you studied.',
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
        'mini_challenge': 'Create a boolean called practiced_today. Use an if statement to print one encouraging message if it is True and another if it is False.',
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
        'mini_challenge': 'Create a variable called temperature. Use if, elif, and else to print one message for hot weather, one for mild weather, and one for cold weather.',
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
        'mini_challenge': 'Create a list of three coding goals and a dictionary with your name, favorite topic, and current practice streak. Print one item from the list and two values from the dictionary.',
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
        'mini_challenge': 'Make a collection of three goals for the week and print each one with a for loop.',
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
        'mini_challenge': 'Create a tuple of three goals for this month and a set of topics you have completed so far. Print both and explain what makes them different.',
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
        'mini_challenge': 'Write a function called celebrate_progress that accepts a name and a completed lesson count. Return one encouraging f-string sentence and print it.',
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


def get_module(slug):
    return next((module for module in MODULES if module['slug'] == slug), None)


def get_lesson(slug):
    return next((lesson for lesson in LESSONS if lesson['slug'] == slug), None)
