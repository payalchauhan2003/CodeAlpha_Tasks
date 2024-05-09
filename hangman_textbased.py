import random

# List of words
words = ['python', 'java', 'javascript', 'html', 'css', 'ruby', 'php']

# Maximum number of incorrect guesses allowed
max_incorrect_guesses = 6
def select_random_word(words):
    return random.choice(words)


def display_game_state(word, guessed_letters, incorrect_guesses):
    # Display the current state of the word with underscores for unguessed letters
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'

    print('Word: ' + ' '.join(display_word))
    print('Incorrect guesses left: ' + str(max_incorrect_guesses - incorrect_guesses))
    print('Guessed letters: ' + ', '.join(guessed_letters))
def get_guess(guessed_letters):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in guessed_letters:
            print('You have already guessed that letter. Try again.')
        elif not guess.isalpha():
            print('Please enter a valid letter.')
        else:
            return guess


def update_game_state(word, guess, guessed_letters, incorrect_guesses):
    if guess in word:
        guessed_letters.add(guess)
    else:
        incorrect_guesses += 1

    return incorrect_guesses
def is_game_over(word, guessed_letters, incorrect_guesses):
    # Check if the player has guessed the word
    if all(letter in guessed_letters for letter in word):
        print('Congratulations! You guessed the word: ' + word)
        return True
    # Check if the player has used up all their incorrect guesses
    if incorrect_guesses >= max_incorrect_guesses:
        print('You have used up all your incorrect guesses.')
        print('The word was: ' + word)
        return True
    return False
def play_again():
    choice = input('Do you want to play again? (yes/no): ').lower()
    return choice == 'yes'


def main():
    print('Welcome to Hangman!')

    while True:
        # Select a random word
        word = select_random_word(words)

        # Initialize game state
        guessed_letters = set()
        incorrect_guesses = 0

        # Game loop
        while True:
            # Display the current state of the game
            display_game_state(word, guessed_letters, incorrect_guesses)

            # Get a guess from the player
            guess = get_guess(guessed_letters)

            # Update the game state based on the guess
            incorrect_guesses = update_game_state(word, guess, guessed_letters, incorrect_guesses)

            # Check if the game is over
            if is_game_over(word, guessed_letters, incorrect_guesses):
                break

        # Ask the player if they want to play again
        if not play_again():
            break

    print('Thank you for playing Hangman!')


# Run the main function
if __name__ == '__main__':
    main()
