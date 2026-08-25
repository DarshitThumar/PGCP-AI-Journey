# Day 2: Number Guessing Game
# PGCP-AI Journey – CDAC Bangalore

import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10:")

while True:
    try:
        guess = int(input("Your guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed it!")
            break
    except ValueError:
        print("Please enter a valid number.")