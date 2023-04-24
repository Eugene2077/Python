# Operators
# < , > , > , = , <= , = , !=

# comparison strings
print("bag" > "apple")  # True, because when we sort these two words, "bag" comes after "apple"
print("bag" > "BAG")   # False, because capital letter comes first in ASCII



# IF ELIF ELSE / TRY EXCEPT

a_number = input("input any number: ")  # input
try:
    a_number = int(a_number)            # try to cast a_number to int
    numeric = True
except:                                 # it the try was not successful
    numeric = False

if not numeric:
    print("Error - invalid input")
else:
    if a_number % 2 == 0:
        print("this number is even")
    else:
        print("the number is odd")


temprature = 11
if temprature < 10:
    print('stay warm')
elif 25 > temprature >= 10:
    print("it's a nice weather")
else:
    print('hot day, drink more water')


# 또는 이런 방식으로 쓸수도 있는데 이를 Ternary Operator 라고 한다.
age = 12
message = "eligible" if age >= 18 else "not eligible"
print(message)


# Logical Operators -----------

'''and, or, nor, !'''

high_income = True
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


# While loop ---------------

'''
secrit_number = 8
guess_limit = 3
guess_count = 0
while guess_limit > guess_count:
    your_guess = int(input('Guess the Number: '))
    guess_count += 1
    if your_guess == secrit_number:
        print('You won')
        break
else:
    print('You failed')
'''
# 아래 예는 while 을 사용하여 차를 시동걸고 끄는 프로그램
'''
user_input = ''
started = False
while True:
    user_input = input('> ').lower()
    if user_input == 'start':
        if started:
            print('Hey what are you doing? Car already started')
        else:
            print('Car started...Ready to go!')
            started = True
    elif user_input == 'stop':
        if not started:
            print('Car is alreasy stopped, are you a moron?')
        else:
            print('Car stopped')
            started = False
    elif user_input == 'help':
        print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
''')
    elif user_input == 'quit':
        break
    else:
        print("I don't understand that")

'''



