from datetime import datetime


hangman_stages=[

'''
 +---+
 |   |
     |
     |
     |
     |
=========
''',

'''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''',

'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''',

'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''',

'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''',

'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''',

'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
'''
]


def save_score(result,word):

    with open(
        "scores.txt",
        "a",
        encoding="utf-8"
    ) as file:

        time=datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        file.write(
            f"[{time}] {result} - {word}\n"
        )