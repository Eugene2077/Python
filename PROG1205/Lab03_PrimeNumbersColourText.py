# Name : Hongju (Eugene) Shin
# Date : 28 Oct 2021
# App Name : Prime Numbers
# App Description: App that display all the prime numbers range from user's input

from os import system
from colorama import Fore, Style
from colorama.ansi import Back # pip install colorama

# Set the console title
system("title Prime Numbers - Hongju(Eugene) Shin")

# Constant
MIN_NUMBER, MAX_NUMBER = 2, 100

# We want to try at least once
restart = "y"

# Restart app if the palyer enters 'r'
while restart == "y":

    # Clear the screen for a new round
    system("cls || clear")

    # Docstrings
    INTRODUCTION = f"""
    =================
    = Prime Numbers =
    =================
    """

    # Introduction
    print(INTRODUCTION)

    # VAlidation loop
    valid = False
    while not valid:
        # Ask the number
        number = input(f"Enter a number between {MIN_NUMBER} and {MAX_NUMBER}): ")

        try:
            number = int(number)
            numeric = True
        except:
            numeric = False

        # Error in case not numeric
        if not numeric:
            print("Error - Input must be a whole number")
        # Error in case not in the valid range
        elif number < MIN_NUMBER or number > MAX_NUMBER:
            print(f"Error - Number must be between {MIN_NUMBER} and {MAX_NUMBER}!")
        # Otherwise it's valid
        else:
            valid = True

    # Now we have a valid number

    # Clear the console screem
    system("cls || clear")

    # Output headline
    output_headline = f"""
    ============================
    == Prime Numbers up to {number} ==
    ============================
    """
    print(output_headline)
    print()  # Adding one space

    # Prime counter: count how many prime numbers in the input number
    prime_counter = 0
    # Calculate prime numbers
    for count in range(MIN_NUMBER,number):           # Check numbers between the MIN_NUMBER and the number
        is_prime = True                              # Assume the number is a prime number
        for test_number in range(MIN_NUMBER,count):  # Check the current number is a prime or not
            if count % test_number == 0:             # if the number is divided, it is not a prime number
                is_prime = False                     # it is not a prime number
        if is_prime:                                 # if the number is not divided in the iteration
            prime_counter += 1                       # count how many prime prime numbers in the input number
            # Print and draw the prime numbers
            print(Back.GREEN,end="")                  # Change draw colour
            for draw_sharp in range(count):          # Drow '#'
                print("#",end="")
            print(Style.RESET_ALL,end="")                   # Reset the colour

            print(" ",count)                         # print prime numbers

    # Display how many prime numbers in the input number
    print()   # Adding one space
    print(f"There are {prime_counter} prime numbers from {MIN_NUMBER} up to {number}")
    print()   # Adding one space

    # Ask the users if they wnat to restart
    restart = input("Enter 'Y' to process another game or [Enter] to exit: ").lower()
    
