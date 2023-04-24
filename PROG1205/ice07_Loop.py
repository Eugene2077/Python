# Name : Hongju (Eugene) Shin
# Date : 14 Oct 2021
# App Name : Factorial
# App Description: App that calculate the F! of a number

from os import system

# Constant
MIN, MAX = 0, 20

# Set the title
system("title Factorial - Hongju(Eugene) Shin")

# False because we want to loop at least ONCE
valid = False

# Validation loop
while not valid:
    # Ask a number
    number = input(f"Enter a number up to {MAX}: ")

    try: 
        # Try to convert from string to int
        number = int(number)
        numeric = True   # Able to convert
    except:
        numeric = False  # Unable to convert

    # In Case number is not a number
    if not numeric:
        print(f"Error - number must be numeric")

    # In case number is NOT between 0 and 20
    elif number < MIN or number > MAX:
        print(f"Error - number must be between {MIN} and {MAX}")

    # now we have a valid number
    else: 
        valid = True

# Calculate the result
result = 1
# Count backward from the input to MIN
for item in range(number, MIN+1,-1):
    result *= item
    
# Print the result
print(f"{number}! = {result}")

# Exit prompt
input("Press [enter] to exit: ")