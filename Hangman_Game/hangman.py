import random
from words import word_categories
from utils import hangman_stages, save_score


class HangmanGame:

    def __init__(self):

        category = random.choice(
            list(word_categories.keys())
        )

        self.word = random.choice(
            word_categories[category]
        ).upper()

        self.category = category

        self.guessed_letters = []
        self.wrong_attempts = 0
        self.max_attempts = 6


    def display_word(self):

        display = ""

        for letter in self.word:

            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        return display


    def play(self):

        print(f"\nCategory: {self.category}")

        while self.wrong_attempts < self.max_attempts:

            print("\n"+hangman_stages[self.wrong_attempts])

            print("\nWord:",self.display_word())

            print(
                "Guessed:",
                ", ".join(self.guessed_letters)
            )

            guess = input(
                "\nEnter a letter or type 'hint': "
            ).upper()


            if guess=="HINT":

                unrevealed=[]

                for letter in self.word:

                    if letter not in self.guessed_letters:
                        unrevealed.append(letter)

                if unrevealed:
                    hint=random.choice(unrevealed)

                    self.guessed_letters.append(
                        hint
                    )

                    print(
                        f"💡 Hint letter: {hint}"
                    )

                continue


            if len(guess)!=1 or not guess.isalpha():

                print(
                    "❌ Enter only one letter"
                )
                continue


            if guess in self.guessed_letters:

                print(
                    "⚠ Already guessed"
                )
                continue


            self.guessed_letters.append(
                guess
            )


            if guess not in self.word:

                self.wrong_attempts +=1

                print(
                    "❌ Wrong guess"
                )

            else:
                print(
                    "✅ Correct"
                )


            completed=True

            for letter in self.word:

                if letter not in self.guessed_letters:
                    completed=False
                    break

            if completed:

                print(
                    "\n🎉 YOU WON!"
                )

                print(
                    "Word was:",
                    self.word
                )

                save_score(
                    "WIN",
                    self.word
                )

                return


        print(
            hangman_stages[-1]
        )

        print(
            "\n💀 YOU LOST"
        )

        print(
            "Correct word:",
            self.word
        )

        save_score(
            "LOSS",
            self.word
        )