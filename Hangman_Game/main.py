from hangman import HangmanGame

def main():

    print("="*50)
    print("🎮 ADVANCED HANGMAN GAME")
    print("="*50)

    while True:

        game = HangmanGame()
        game.play()

        choice = input("\nPlay again? (yes/no): ").lower()

        if choice != "yes":
            print("Thanks for playing 👋")
            break


if __name__ == "__main__":
    main()