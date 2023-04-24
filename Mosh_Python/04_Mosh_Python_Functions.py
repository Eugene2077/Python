print("define function ----------------------")


def greet(a, b):
    print(a, b)


greet("fuck", 12)

# There are two types of functions
# 1. Perform a task : 위 예처럼 정해진 작업을 수행
# 2. Return a value : function 에 return 을 삽입하여 원하는 값을 return
# python 에서 모든 function 은 return 값을 별로도 지정하지 않으면 'none' 을 return 한다..


def increment(number, by):
    return number + by


# keyword argument
# 아래 예에서 (number=, by=)가 필요하지는 않지만 readability 를 위해 삽입가능
print(increment(number=2, by=1))

print("default argument ----------------------")
# 아래 예에서 하나의 argument 값을 default argument 로 사전지정한 모습


def increse(number, by=5):  # 주의할점은 optional parameter들은 항상 뒤쪽으로 와야한다는 점
    # (그렇지않으면 passing 되는 argument중 어떤게 default 에 해당하는지 알수가 없슴)
    return number + by


print(increse(2, 2))


print("undefined arguments(tuple) ----------------------")
# 아래와 같이 parameter를 '*name' 으로 쓰고, 임의의 갯수로 argument들을 받아들일 수 있다.


def multiply(*a):  # 이렇게 받아들인 argument 들은 tuple 형태로 저장된다.
    return(a)     # argument 갯수가 불특정이기 때문에 많은경우 for, while 등 iteration 을 사용해야 할듯


the_value = multiply(1, 2, 3, 4)
print(type(the_value))
print(the_value)

print("undefined argments(dictionary) ----------------------")
# 아래와 같이 parameter에 '**name' 으로 쓰는 경우, data를 dictionary 로 받아들임


def users(**a):       # 이렇게 받아들인 argument 들은 dictionary 형태로 저장된다.
    return(a["age"])  # bracket notation 을 사용하여 원하는 value 만을 사용할 수 있다..


this_value = users(id=1, name="John", age=44)
print(this_value)

print("scope -------------------------------------------")
# even if there is a same variable name inside a function as a gloval variable, these two
# considered as different ones because one is gloval and the other is local, so if you try
# to change the value of a gloval variable inside of a function, it does not work. if you
# wanna change a gloval variable inside a functin you can use the function 'gloval variable_name'
# but it is strongly not recommended to use like this because it will cause maintenance problems.
# the best practice is use gloval variable as least as you can.
