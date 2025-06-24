import random

def hangman():
    words = ["apple", "python", "garden", "simple", "planet"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print("Word:", " ".join(display_word))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word:
            guessed_letters.append(guess)
            if set(secret_word) <= set(guessed_letters):
                print("Congratulations! You guessed the word:", secret_word)
                break
        else:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")
    else:
        print("Sorry, you're out of attempts. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
