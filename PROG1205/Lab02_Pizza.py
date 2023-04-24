
# Name : Hongju (Eugene) Shin
# Date : 08 Oct 2021
# App Name : Pizza Cut
# App Description: This App is about cutting given size pizza

from os import system
import math

# Contants
MIN_SIZE, MAX_SIZE = 8, 24

# Set the console title
system("title Pizza Cut- Hongju(Eugene) Shin")

# ask for the diameter
diameter = input("Please enter the diameter of your pizza: ")

# Try to convert from string to integer
try:
    diameter = int(diameter)
    numeric = True        # Able to convert
except:
    numeric = False       # Unable to convert

# If the diameter is not numeric, then print an error
if not numeric:
    print("Error - Diameter must be numeric!")
# Print an error if the input is ouside of the range
elif diameter < MIN_SIZE or diameter > MAX_SIZE:
    print(f'Error - Pizza must have a diameter in the range of {MIN_SIZE}" to {MAX_SIZE}" inclusive! ')
# When the input is valid, determine the slices
else:
    cut = 0
    if diameter < 12:
        cut = 6
    elif diameter < 14:
        cut = 8
    elif diameter < 16:
        cut = 10
    elif diameter < 20:
        cut = 12
    else:
        cut = 16

    # Calculate the area
    area = math.pi * (diameter/2)**2   # area calculation
    area = round(area, 2)               # rounding

    # Calculate the slice
    angle = int(round(360/cut))        # the angle calculation / round to int
    slice_area = round(area/cut, 2)     # slice calculation / round to 2 digits

    # Output
    print(f'A {diameter}" pizza has an area of {area} square inches and will yield {cut} slices.')
    print(
        f'Each slice will be cut at {angle} degrees and have an area of {slice_area} square inches.')

# Exit prompt
input("Press [enter] to end this application")
