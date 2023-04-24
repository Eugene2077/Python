# Name : Hongju (Eugene) Shin
# Date : 18 Nov 2021
# App Name : Bowling Scores
# App Description: App that calculate 6 bowler's scores

from os import system

# Set the console title
system("title Bowling Scores - Hongju(Eugene) Shin")

# Constant
MIN_SCORE, MAX_SCORE = 0, 300
NUM_OF_BOWLERS = 6


# We want to try at least once
restart = "y"

# Restart app if the palyer enters 'y'
while restart == "y":

    system("cls || clear")
 
    # set an empty list
    score_list = [None] * NUM_OF_BOWLERS

    # A loop for get the valid inputs from the user
    for list_element in range(NUM_OF_BOWLERS):    # we need 6 input value
        input_confirmed = False                   # set the initial value

        # Input and validation loop
        while input_confirmed == False:                # as long as the input is not confirmdd, keep loop
            input_score = input(f"Score of Bowler {list_element+1}: ")  # input from the user

            # input validation
            try:
                input_score = int(input_score)         # try to casting to int
            except:
                print("Error: Score must be numeric!") # it not successful
                continue                               # the input loop again
            if input_score < MIN_SCORE or input_score > MAX_SCORE:   # Check if the number is in the range
                print(f"Error: Score must be between {MIN_SCORE} and {MAX_SCORE}!") # out of range message
            # If the input is valid number    
            else:  
                score_list[list_element] = input_score  # put the valid user's input to the score_list variable
                input_confirmed = True                  # the Input and validation loop is over

    # until here, we have the list of the valid scores 

    # Calculation 

    # variavles initialization 
    score_highst = MIN_SCORE   # highst score
    score_lowest = MAX_SCORE   # lowest score
    score_sum = MIN_SCORE      # sum of the all scores

    for score in score_list:       # loop for finding which is highst and lowest
        if score > score_highst:   # if the item is higher than the previous highet
            score_highst = score   # replace to the new value
        if score < score_lowest:   # if the item is lower than the previous lowest
            score_lowest = score   # replace to the new value
        score_sum += score         # sum calculation

    score_average = round(score_sum/NUM_OF_BOWLERS)  # average calculation

    # finding which player was the highest and lowest
    # creat the winners and losers lists
    highst_bowlers = [None] * NUM_OF_BOWLERS
    lowest_bowlers = [None] * NUM_OF_BOWLERS

    # this for loop is for finding which bowlers were the highst and lowest scored    
    for index in range(NUM_OF_BOWLERS):        # Loop for finding who's score was
        if score_list[index] == score_highst:  # if current score is the same as the highst score
            highst_bowlers[index] = index + 1  # this bowler was the highst scored one

        if score_list[index] == score_lowest:  # if current score is the same as the lowest score
            lowest_bowlers[index] = index + 1  # this bowler was the lowest scored one
    # New we have two lists about highst and lowest players

    # We want to know if the winners and losers are more than one, because we wanna print the correct plural grammar
    number_of_winners = 0           # initialize a variable to get how many winners in the list
    for item in highst_bowlers:     # loop for counting the winners
        if item != None:            # if there is a value
            number_of_winners += 1  # count +1
    if number_of_winners == 1:      # if the winner is only one
        solo_winner = True
    else:                           # if the winners are more than one
        solo_winner = False

    number_of_losers = 0            # initialize a variable to get how many losers in the list
    for item in lowest_bowlers:     # loop for counting the winners
        if item != None:            # if there is a value
            number_of_losers += 1   # count +1
    if number_of_losers == 1:       # if the loser is only one
        solo_loser = True
    else:                           # if the losers are more than one
        solo_loser = False



    # Clear the screen for displying the result
    system("cls || clear")
    # print the headline
    print("""
========================================================
                  Bowling Game Scores
--------------------------------------------------------
    """)
    # print the scores of each player
    for index,item in enumerate(score_list):
        print(f"  B{index+1}: {item}",end="")

    print("""
--------------------------------------------------------
    """)
    # print the average score
    print(f"Average score in this game is {score_average} points")


    # print the highst scored bowlers (winners)
    if solo_winner:                # when the winner is only one
        print("Bowler ",end="")
    else:                          # when the winners are more than one
        print("Bowlers ",end="")

    # Loop for printing ones that have value
    for item in range(NUM_OF_BOWLERS):     # for loop
        if highst_bowlers[item] != None:   # if the item has a value
            print(f"B{item+1} ",end="")

    # print the rest
    if solo_winner:                 # when the winner is only one
        print("is the winner")
    else:                           # when the winners are more than one
        print("are the winners")


    # print the lowest scored bowlers (losers)
    if solo_loser:
        print("Bowler ",end="")
    else:
        print("Bowlers ",end="")
        
    # Loop for printing ones that have value
    for item in range(NUM_OF_BOWLERS):     # for loop
        if lowest_bowlers[item] != None:   # if the item has a value
            print(f"B{item+1} ",end="")
    # print the rest
    if solo_loser:
        print("is the loser")
    else:
        print("are the losers")

    print("""
========================================================
    """)




    # Ask the users if they wnat to restart
    restart = input("Enter 'Y' to process another game or [Enter] to exit: ").lower()