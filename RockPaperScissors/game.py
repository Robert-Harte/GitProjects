# Rock Paper Scissors game implementation
import random

choices = ["r", "p", "s"]   # The three choices. r = rock, p = paper, s = scissors
rounds_played = 0     #   number of rounds played.
num_rounds = 0
player_wins = 0
comp_wins = 0

try:
    num_rounds = int(input("Enter number of rounds to play: "))     #   ask user how many rounds to play
    if num_rounds <= 0:
        num_rounds = 1  # default to 1 round
        print("Number of rounds must be greater than 0. Setting to 1 round.")
    # Loop until all the rounds are played. Only winning rounds count.
    while rounds_played < num_rounds:
        user_choice = input("Select a choice (Rock (R), Paper (P) or Scissors (S)): ").lower()  # set to lower case to match choices list.
        if user_choice not in choices:  # if invalid choice, skip rest of loop.
            print(f"Error! Your choice of {user_choice} is not valid!")
            pass
        computer = random.choice(choices)   #   set random value for the computer
        if ((user_choice == "r" and computer == "s") or (user_choice == "s" and computer == "p") or (user_choice == "p" and computer == "r")):
            player_wins += 1
            print("You win!")
        elif ((user_choice == "s" and computer == "r") or (user_choice == "p" and computer == "s") or (user_choice == "r" and computer == "p")):
            comp_wins += 1
            print("You lost!")
        else:
            print("Draw!")
            pass
        rounds_played += 1
    print(f"Player wins: {player_wins}. Computer wins: {comp_wins}")
    
except ValueError:
    print(f"You idiot! {num_rounds} is not a valid number. Ending program")