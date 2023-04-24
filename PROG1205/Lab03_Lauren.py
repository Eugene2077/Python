












prime = True    # initial set
for count in range(2,user_input+1):       # check the numbers one by one
    for num in range(MIN_NUMBER, count):  # check if the current number is prime or not
        if count % num == 0:              # if the current number is divided by a number between MIN to current number
            prime = False                 # this number is not a prime
    
    if prime:
    # draw sharps and print number below