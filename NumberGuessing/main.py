# Number guessing game
# Generate a random number.
# Allow user to input a number to guess
# Respond if successful or not

import random

number = random.randint(1, 100)     # random number between 1 and 100

# keep looping until the correct number is guessed
while True:
    try:
        guess = int(input("Guess a number: "))
        if (guess <= 0) or (guess > 100):
            print("Invalid number. Value must be between 1-100")
        elif guess == number:
            print(f"You win! Number was: {number}")
            break
        elif guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    except ValueError:
        print("The value you entered was not a number!")