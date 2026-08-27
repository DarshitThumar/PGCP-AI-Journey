# Day 3: Rock-Paper-Scissors Game
# PGCP-AI Journey – CDAC Bangalore

import random 

def play():
    # Define possible choices
    choices = ["rock", "paper", "scissors"]

    # Computer randomly picks one choice
    computer = random.choice(choices)

    # Ask user for input
    user = input("Enter your choice (rock/paper/scissors): ").lower()

    # Validate user input
    if user not in choices:
        print("Invalid choice! Please try again.")
        return  # Exit function if input is invalid

    # Show computer's choice
    print(f"Computer chose: {computer}")

    # Compare user vs computer
    if user == computer:
        print("It's a tie!")  # Same choice
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")  # Winning conditions
    else:
        print("You lose!")  # All other cases are losses

play()
