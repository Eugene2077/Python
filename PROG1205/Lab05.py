# Name : 
# Date : 
# App Name : Caesar Cipher
# App Description: App that encript and decript the message from the user's input

from os import system

system("title Caesar Cipher - ")

ENCRIPTION_KEY = 200
ENCRIPT = "1"
DECRIPT = "2"
QUIT = "3"


def encription(message):
    """function for encription, parameter:strings to encript """
    message_encrypt = ""

    for letters in message:
        message_encrypt += chr(ord(letters) + ENCRIPTION_KEY)

    return(message_encrypt)


def decription(message):
    """function for decription, parameter: strings to decript"""
    message_decrypt = ""
    for letters in message:
        message_decrypt += chr(ord(letters) - ENCRIPTION_KEY)
    return(message_decrypt)


INTRODUCTION = f"""

~~~~~~~~~~~~~~~~
~ Caesar Ciper ~
~~~~~~~~~~~~~~~~

This app will encript/decript a secret message using the Caesar Ciper.

Choose an option:
1. Encript a message
2. Decript a message
3. Quit app """


while True:          
    system("cls || clear") 

    print(INTRODUCTION)         
    user_selection = input(" > ")    
    if user_selection == ENCRIPT:    
        message = input("\nEnter a secret message to encript: ")
        encripted_message = encription(message)
        print(f"Encripted code: ", encripted_message)

    elif user_selection == DECRIPT:  
        message = input("\nEnter a code to decript: ")

        decripted_message = decription(message)
        print(f"Decripted message: ", decripted_message)

    elif user_selection == QUIT:
        exit()

    else:
        print("Error - Invalid option!")
    input("\nPress [enter] to continue:")

input("\nPress [enter] to exit: ")
