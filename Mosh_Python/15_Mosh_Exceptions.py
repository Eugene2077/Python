
# Exceptions

try:                                    # when you try something at here
    file = open("01.Mosh_Python_Basics.py")  # if you open a file, you will need to close the file after use.
    age = int(input("age: "))           # input age
    something = 10 / age                # something divided by input
except ValueError as ex:                # when there is a Value Error, this is executed
    print("you didn enter a valid age") # 
    print(ex)                           # print what is the error
    print(type(ex))                     # print type of error
except ZeroDivisionError:               # when there is a zero division error(when you try something divide by zero)
    print("age cannot be 0.")
else:                                   # when there is no error this execute
    print("no exception orro")
finally:                                # when you don't need the file anymore, closing the file at here
    file.close()                        # finally는 에러가 있던지 없던지간에 항상 실행해야 할 경우 사용


