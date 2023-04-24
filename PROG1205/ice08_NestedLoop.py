# Name : Hongju (Eugene) Shin
# Date : 28 Oct 2021
# App Name : Pyramid
# App Description: App that prodeduranlly generates a pyramid

from os import system
# from colorama import Fore, Style # pip install colorama

# Set the console title
system("title Pyramid Generator - Hongju(Eugene) Shin")
 
# Constant
MIN_HEIGHT, MAX_HEIGHT = 5, 50
PYRAMID_START = 1

# Docstring - Mumbiline string5hk
INTRODUCTION = f"""
===========
= Pyramid =
===========

Yo! Do you want to draw a dope Pyramid?
Just let me know how tall and I will draw it for you!
"""

# Introduction
print(INTRODUCTION)

# VAlidation loop
valid = False
while not valid:
    # Ask the height
    height = input(f"Enter the height(min {MIN_HEIGHT}, max {MAX_HEIGHT}): ")

    try:
        height = int(height)
        numeric = True
    except:
        numeric = False

    # Error in case not numeric
    if not numeric:
        print("Error - height must be a number")
    # Error in case not in the valid range
    elif height < MIN_HEIGHT or height > MAX_HEIGHT:
        print(f"Error - Height must be between {MIN_HEIGHT} and {MAX_HEIGHT}!") 
    # Otherwise it's valid
    else: 
        valid = True

print()  # Adding one space

# Draw the Pyramid
for count_line in range(PYRAMID_START,height+1):
    # Line counter  - : 2 means use 2 spaces
    print(f"{count_line:2} ", end="")  # end=""  means keep printing in the same line

    # Calculate how many spaces
    spaces = height - count_line 
    # Draw spaces
    for count in range(0,spaces+1):
        print(" ", end="")

    # Draw the asterisk (stars)
    for starts in range(count_line):
        print("* ", end="")

    # Finish the line
    print() # by default a print will end with a new line


# Exit prompt
input("\nPress [enter] to exit: ")