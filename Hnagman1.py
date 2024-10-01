import random

def hangman():
    # List of words
    words = ['nexariza', 'internship', 'python', 'project', 'internee']
    
    # Choose a random word from the list
    word = random.choice(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')  # Set of all alphabets
    guessed_letters = set()  # Letters the user has guessed
    
    lives = 6  # Number of lives
    
    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and lives > 0:
        # Show current guessed letters and word progress
        print(f"\nYou have {lives} lives left and have guessed these letters: {' '.join(guessed_letters)}")
        
        # Show the current state of the word
        word_progress = [letter if letter in guessed_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_progress))
        
        # Get user input
        user_guess = input('Guess a letter: ').lower()
        
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            
            if user_guess in word_letters:
                word_letters.remove(user_guess)
                print(f'Good job! {user_guess} is in the word.')
            else:
                lives -= 1
                print(f'{user_guess} is not in the word. You lose a life.')
        elif user_guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        else:
            print('Invalid input. Please enter a valid letter.')
    
    if lives == 0:
        print(f'\nSorry, you lost! The word was {word}.')
    else:
        print(f'\nCongratulations! You guessed the word {word} correctly!')

# Start the game
hangman()
