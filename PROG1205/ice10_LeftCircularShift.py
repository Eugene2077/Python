# Name : Hongju (Eugene) Shin
# Date : 011 Nov 2021
# App Name : Left Circular Shift
# App Description: App that shift circular to the left from the list from user's input

from os import access, system
from typing import Iterable

# Set the console title
system("title Left Shift - Hongju(Eugene) Shin")

# We want to try at least once
restart = "r"

# Restart app if the palyer enters 'r'
while restart == "r":

    # Clear the console screem
    system("cls || clear")

    # Greetings
    print("""
    =========================
    == Left Circular Shift ==
    =========================
    """)


    # input from a user
    elements = input("Enter elements divided by spaces: ").split(" ")

    # input validation
    accept_input = False     # until validated, it is false
    while not accept_input:
        shifts = input("Enter number of shifts: ")

        # try to convert to int
        try:  
            shifts = int(shifts)
            numeric = True
        except:
            numeric = False

        # the input is valid only when it is a natural number
        accept_input = numeric and (shifts > 0)
        # when the input is not valid
        if not accept_input:
            print("Error - Shifts must be a positive whole number!!")

    # Once the validation is done, Go next to the logic part

    # loop as many times as given shifts
    for count_shifts in range(0, shifts):
        # we need to copy the original fist element from the list
        original_first = elements[0]

        # shift the elements of the list to the left
        # Go through all indices of the list
        for index in range(len(elements)-1):
            # copy the next element into the current index
            elements[index] = elements[index+1]
            # current element = next element
        
        # put first element in the last slot
        elements[len(elements)-1] = original_first
    
    # print the list called elements
    # ["a","b","c"]
    for element in elements:
        # print the element
        print(element, end=" ")  # element + space


    # Ask the users if they wnat to restart
    restart = input("Enter 'R' to restart: ").lower()




# -------------------------------------------------------
# another solutions

# ------ using append()
# stringLen = len(elements)
# shifted = []
# for item in range(stringLen):
#     shifted.append(elements[(item + shifts) % stringLen])
# print(shifted)


# ------using [::]

# shiftedList = elements[shifts:] + elements[:shifts]
# print(shiftedList)

