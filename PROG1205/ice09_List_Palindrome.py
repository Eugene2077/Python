# Name : Hongju (Eugene) Shin
# Date : 06 Nov 2021
# App Name : Palindrome
# App Description: App that tells the user if the input word or phrase is a palindrome or not

from os import system

# Set the console title
system("title Palindrome - Hongju(Eugene) Shin")

# We want to try at least once
restart = "r"

# Restart app if the palyer enters 'r'
while restart == "r":

    # Clear the console screem
    system("cls || clear")

    # input from a user
    word = input("Enter a word or phrase: ")

    # set the input forward order to a list
    word_to_list = []
    # set the input backward order to a list
    reverse = []

    # chracters to remove
    chracters_to_remove = (" ",",",".","'","\"","?","!")

    # Loop for creating a list of reverse of the input
    for chracter in word.lower():             # to lowercase and iterate them 
        if chracter in chracters_to_remove:   # if the chractor is one of the remove list, skip it
            continue                          # skip
        reverse.insert(0,chracter)            # put the words at the beginning of the list --> make reverse order list from a string

    # Loop for creating a list of the input
    for chracter in word.lower():              # to lowercase and iterate them 
        if chracter in chracters_to_remove:    # if the chractor is one of the remove list, skip it
            continue
        word_to_list.append(chracter)          # put the words at the end of the list --> make to a list from a string

    # if the forward and reverse words are match, 
    if word_to_list == reverse:
        print(f"{word} is a palindrome.")

    # if the forward and reverse words are NOT match
    else:
        print(f"{word} is NOT a palindrome.")

    # Ask the users if they wnat to restart
    restart = input("Enter 'R' to restart: ").lower()