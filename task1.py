import random

# List of 5 predefined words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")

# Game loop
while incorrect_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player won
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Get user's guess
    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guess
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")
        print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

# If player loses
else:
    print("\n😢 Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")

