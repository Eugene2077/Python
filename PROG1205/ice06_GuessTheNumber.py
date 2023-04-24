# Name : Hongju (Eugene) Shin
# Date : 06 Sep 2021
# App Name : Guess The Number
# App Description: Game that the player has to guess a secret random number

from os import system
import random  # import the random number methods

# Constant
MIN_NUMBER, MAX_NUMBER = 1, 100

# Set the console title
system("title Guess The Number - Hongju(Eugene) Shin")

# We want to paly at least once !
restart = "r"

# Restart the game if the palyer enters 'r'
while restart == "r":
    # Prepare for a new game
    # Clear the screen for a new game
    system("cls")

    # Generate a secret random number
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    # start with 0 attempt
    attempt = 0

    # Start with a guess that is not valid, so we can play
    guess = 0

    # keep  playing until the player guesses the secret number!
    while guess != secret_number:
        # Prompt for a number
        guess = input(f"Pick a number between {MIN_NUMBER} and {MAX_NUMBER}: ")

        # Try to convert the guess into an integer
        try:
            guess = int(guess)
            numeric = True     # Able to convert
        except:
            numeric = False    # Unable to convert

        # Print an error in case the guess is not numeric
        if not numeric:
            print(f"Error - You must select a number between {MIN_NUMBER} and {MAX_NUMBER}")
        
        # Valid guess
        else:
            # Add 1 to the attempt
            attempt += 1

            # Give the player a hint
            # Guess is too high
            if guess > secret_number:
                print(f"{guess} is too high")
            # Guess is too low
            elif guess < secret_number:
                print(f"{guess} is too low")
            
    # Only reaches this point when the player wins
    print(f"Hurray! Yes the number is {guess}!")
    print(f"You guessed in {attempt} attempts")
    
    # Ask the player if they wnat to restart
    restart = input("Enter 'r' to restart: ")
