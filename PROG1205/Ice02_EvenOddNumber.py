# Name : Hongju (Eugene) Shin
# Date : 20 Sep 2021
# App Name : Even Odd Number
# App Description: This app decide if a number is even or odd

# import more codes into this program (such as writing the title below )
from os import system

# Set the console title
system("title Even Odd Number - Hongju(Eugene) Shin")

# Ask for a number
number = input("Enter a whole number: ")  # this input only get with string type

# Try to convert into an int
try:
    number = int(number)
    numeric = True   # able to convert
except:
    numeric = False  # unable to convert

# This will only excute if the input is invalid
if not numeric:  
    print("Error - Invalid input")
    input("Press ENTER to exit")

# Only calculate if the input is valid
else:
    # Check if the number is divisible by 2
    remainder = number % 2  # will be 0 if the number is evenly divisible by 2

    # Decide if the number is even or odd

    # Check if the remainder is 0
    if remainder == 0:
        print(f"The number {number} is even") # f for formatted string

    # The remainder is not 0
    else:
        print(f"The number {number} is odd") # f for formatted string
    # Exit prompt
    input("Press ENTER to exit")