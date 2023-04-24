
# Name : Hongju (Eugene) Shin
# Date : 30 Sep 2021
# App Name : Dice Bet
# App Description: Game that players must guess the result of 2 dice

from os import system, truncate
import random  # Allow us to generate random numbers

# Set the console title
system("title Dice Bet - Hongju(Eugene) Shin")

# Contants
MIN_BET, MAX_BET = 2, 12
MIN_ROLL, MAX_ROLL = 1, 6

# Ask the user to place a bet
bet = input(f"Place your bet between {MIN_BET} and {MAX_BET}: ")

# Try to convert from string to integer
try:
    bet = int(bet)
    numeric = True  # Able to convert
except:
    numeric = False # Unable to convert

# If the bet is not numeric, then print an error
if not numeric:
    print("Error - Bet must be numeric")

# If the bet is not in the valid range, then print an error
# and - Both condition must be true
# or - just need one of the condition to be true
elif MIN_BET > bet or bet > MAX_BET:
    print(f"Error - Bet must be between {MIN_BET} and {MAX_BET}")

# Valid bet - we can play now
else:
    print("Rolling dice !")
    # Generate two random numbers !
    dice_one = random.randint(MIN_ROLL, MAX_ROLL)
    dice_two = random.randint(MIN_ROLL, MAX_ROLL)

    # Add the dice result and store the result in a variable
    outcome = dice_one + dice_two

    # Print the bet and the dice result
    print(f"Your bet: {bet}")
    print(f"Dice Result: {dice_one} + {dice_two} = {outcome}")

    # Decide if the player wins or loses
    # Player guesses the number, print "you WIN" if the bet is right, print "You lose" in else cases
    print("You WIN! :D") if bet == outcome else print("You lose :(")

# Exit prompt
input("Press [Enter] to exit")
