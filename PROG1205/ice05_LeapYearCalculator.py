# Name : Hongju (Eugene) Shin
# Date : 30 Sep 2021
# App Name : Leap Year Calculator
# App Description: This App determines if a given year is leap or not

from os import system

# Set the console title
system("title Leap Year Calculator - Hongju(Eugene) Shin")

# Prompt for a year
year = input("Enter a year that's not 0: ")

# Try to convert year to int (whole numbers)
try:
    year = int(year)
    numeric = True   # Able to convert
except:
    numeric = False  # Unable to convert

# Print an error in case year is not numeric
if not numeric:
    print("Error - Year must be a whole number!")

# Print an error in case year is 0
elif year == 0:
    print("Error - Year cannot be zero!") 

else:
    # To be a leap year: divisible by 4 and (not divisible by 100 or divisible by 400)
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"{year} is a leap year!")

    # When abobe condition is not fulfilled 
    else:
        print(f"{year} is not a leap year!")

# Exit prompt
input("Press [Enter] to exit")