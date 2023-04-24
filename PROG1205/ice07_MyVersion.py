# Name : Hongju (Eugene) Shin
# Date : 14 Oct 2021
# App Name : Factorial
# App Description: App that calculate the F! of a number

from os import system

# Constant
MAX = 20

# Set the title
system("title Factorial - Hongju(Eugene) Shin")

while True:
    number = input(f"input a number less than {MAX}: ")
   
    # Validation
    try:
        number = int(number)
        numeric = True
    except:
        numeric = False

    if not numeric:
        print(f"Error - Please input a natural number less than {MAX}")
        continue

    if number >= 20 or number < 1:
        print(f"Error - Please input a number between 1 to {MAX-1}")
        continue

    # Calculate the result
    result = 1
    for item in range(1,number+1):
        result *= item
    
    # Print the result
    print(f"{number}! = {result}")
    break

# Exit prompt
input("Press [enter] to exit: ")