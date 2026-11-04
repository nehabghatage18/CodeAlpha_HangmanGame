import random

# List of predefined words
words = ["python", "laptop", "coding", "apple", "computer"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN       ")
print("================================")

# Main game loop
while incorrect_guesses < max_attempts:

    print("\nWord: ", end="")

    # Display guessed letters and blanks
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print("\nIncorrect guesses:", incorrect_guesses)
    print("Remaining attempts:", max_attempts - incorrect_guesses)

    # Get input from player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter!")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
        guessed_letters.append(guess)

    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        incorrect_guesses += 1

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("YOU WIN!")
        break

# Check losing condition
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
    print("Better luck next time!")

print("\nThank you for playing Hangman!")