# Name : Hongju (Eugene) Shin
# Date : 04 Nov 2021
# App Name : Caesar Cipher
# App Description: App that encript and decript the message from user's input

from os import system

# Set the console title
system("title Caesar Cipher - Hongju(Eugene) Shin")

# Constant
ENCRIPTION_KEY = 200
ENCRIPT = "1"
DECRIPT = "2"
QUIT = "3"


# functions ----------------------------------

def encription(message):
    """function for encription, parameter:strings to encript """
    # an empty variable
    encripted_message = ""
    # loop for Caesar ciper: done by shifting the letters in the strigngs,
    for letters in message:
        # encript the letters by getting it's numeric value and adding the ENCRIPTION_KEY
        encripted_message += chr(ord(letters) + ENCRIPTION_KEY)
    # return the encripted message
    return(encripted_message)


def decription(message):
    """function for decription, parameter: strings to decript"""
    # an empty variable
    decripted_message = ""
    # loop for Caesar ciper: done by shifting the letters in the strigngs,
    for letters in message:
        # decript the letters by getting it's numeric value and subtracting the ENCRIPTION_KEY
        decripted_message += chr(ord(letters) - ENCRIPTION_KEY)
    # return the encripted message
    return(decripted_message)

# ---------------------------------------------

# Docstring
INTRODUCTION = f"""

~~~~~~~~~~~~~~~~~
~ Caesar Ciper ~
~~~~~~~~~~~~~~~~~

This app will encript/decript a secret message using the Caesar Ciper.

Choose an option:
1. Encript a message
2. Decript a message
3. Quit app """

# selection input loop

while True:          # input loop, keep going until the input is valid
    system("cls || clear")           # clear the screen in a new loop
    # Introduction
    print(INTRODUCTION)              # print intro docstrings
    # user selection input
    user_selection = input(" > ")    # user's selection, what task to do

    if user_selection == ENCRIPT:    # if the user select encription
        # get a messaga to encript
        message = input("\nEnter a secret message to encript: ")
        # function encription call (argument: user's input message)
        encripted_text = encription(message)
        print(f"Encripted code: ", encripted_text)
        # break                        # loop end

    elif user_selection == DECRIPT:  # if the user select decription
        message = input("\nEnter a code to decript: ")
        # function decription call (argument: user's encripted message)
        decripted_text = decription(message)
        print(f"Decripted message: ", decripted_text)
        # break                        # loop end

    elif user_selection == QUIT:
        exit()

    else:
        print("Error - Invalid option!")
    input("\nPress [enter] to continue:")


# Exit prompt
input("\nPress [enter] to exit: ")
