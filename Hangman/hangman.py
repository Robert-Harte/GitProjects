# Game of hangman!
# Randomly select a word.
# Allow user to input a letter
# If letter is part of word, reveal letter. If not, increment failures.
# Game is over if the word is guessed of failures reaches max
# For each letter guessed, track it. Display list of guessed words.

import wordlist
import random


words = wordlist.animals        #   copy list of words to local variable
word = random.choice(words).lower()    #   select random word from wordlist
guesses = []                    #   List of words guessed. Empty for now.
wrong_guesses = 0                 #   Initialise nuimber of guesses.
hangman = ["_" for _ in range(len(word))]   #   Create a list to display the word.

while True:
    print(hangman)
    guess = input("Enter a letter: ").lower()
    
    # Check if the letter has already been guessed
    if guess in guesses:
        print("You have already guessed this letter!")
        wrong_guesses += 1
    
    # Check if the letter is in the word.
    if guess in word:
        # Reveal the letter by adding it to the hangman list
        for i, letter in enumerate(word):
            if guess == letter:
                hangman[i] = guess
    else:
        wrong_guesses += 1
    
    # Check if there are no more letters the guess
    if "_" not in hangman:
        print(f"You win! You guessed the word {word}")
        break
    
    # If too many wrong guesses, break loop and end game
    if wrong_guesses >= 6:      
        print(f"Game over! You suck!. The word was {word}.")
        break