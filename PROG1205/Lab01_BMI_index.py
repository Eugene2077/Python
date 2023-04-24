# Name : Hongju (Eugene) Shin
# Date : 22 Sep 2021
# App Name : BMI Mass Index
# App Description: App that will calculate BMI index

from os import system

# BMI category indexes
SEVERELY_UNDERWEIGHT = 16
UNDERWEIGHT = 18.5
OVERWEIGHT = 25
OBESE = 30

# Set the console title
system("title BMI calculator - Hongju(Eugene) Shin")

# Ask for the height and weight
height = input("Enter your height in feet and inches: ")   # ex) "5 75"
weight = input("Enter the person's weight in pounds: ")    # ex) 173

# Convert the string inputs to numeric values
try:
    # tries to split the input height into 2 variables
    height_feet, height_inches = height.split()

    # try to convert the height in feet into a number (no need decimal)
    height_feet = int(height_feet)
    # try to convert the height in inches into a number (can use decimal )
    height_inches = float(height_inches)
    # convert the height to inches-only
    height = (height_feet * 12) + height_inches

    # try to convert the weight into a number (can use decimal )
    weight = float(weight)

except:
    # did not work
    print("Error - Invalid input")
# For this lab, assume the user will input valid and reasonable numeric data, So validation check is ommited

# Calculation BMI number
bmi = (weight / height**2) * 703
# Round the result to one decimal places
bmi = round(bmi, 1)

# Calculation BMI category
if bmi < SEVERELY_UNDERWEIGHT:          # lower than SEVERELY_UNDERWEIGHT index
    bmi_catetory = "Severy Underweight"  
elif bmi < UNDERWEIGHT:                 # lower than UNDERWEIGHT index
    bmi_catetory = "Underweight"                
elif bmi >= OBESE:                      # higher than OBESE index
    bmi_catetory = "Obese"                           
elif bmi >= OVERWEIGHT:                 # highet than OVERWEIGHT index
    bmi_catetory = "Overweight"                 
else:                                   # between UNDERWEIGHT and OVERWEIGHT
    bmi_catetory = "Healthy"

# Display the result as a formatted string message
print(
    f'The BMI for a {height}" tall person who weights {weight} lb is {bmi}, which is considered "{bmi_catetory}".')

# Exit prompt
input("Press [enter] to exit: ")
