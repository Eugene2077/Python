# Name : Hongju (Eugene) Shin
# Date : 22 Sep 2021
# App Name : Length Converter
# App Description: App that will convert length from centimeters to inches and vice versa

from os import system

# Constant - for values that do not change
CONVERSION_FACTOR = 2.54

# Set the console title
system("title Length Converter - Hongju(Eugene) Shin")

# Ask for the length and unit
length_unit = input("Enter length and unit: ")   # ex) "5 cm"

# If - else for commands that can fail (break the app)
try:
    # tries to split the input into 2 variables
    length, unit = length_unit.split()
    # try to convert the length into a number (can use decimal )
    length = float(length)
    # worked!
    valid = True

except:
    # did not work
    valid = False

# Write an error in case the input is not valid
if not valid:
    print("Error - Invalid input")
    
# In case it's valid then do the calculations

# In case the input is in inches, then convert to centimeters
elif unit == "in":
    # convert to centimeters
    output = length * CONVERSION_FACTOR
    # round the result to 2 decimal places
    output = round(output,2)
    # print the result
    print(f"{length} in corresponds to {output} cm")

# In case the input is in centimeters, then convert to inches
elif unit == "cm":
    # convert to inches
    output = length / CONVERSION_FACTOR
    # round the result to 2 decimal places
    output = round(output,2)
    # print the result
    print(f"{length} cm corresponds to {output} in")

# Invalid unit - write an error
# The else is excuted when all above 'if' are false
else:
    print ("Error - Invalid conversion unit")


# Exit prompt
input("Press [enter] to exit: ")