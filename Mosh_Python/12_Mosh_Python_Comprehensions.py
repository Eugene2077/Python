
# List Comprehensions --------------------------------------------
# Python 에는 List Comprehensions 이라는 게 있는데, 
# 기존 list values 로부터 새로운 list를 만드는 경우 간략히 줄여서 표현할 수 있다.
# 예를 들어 아래 과일 list 로부터 "a"가 포함된 과일명만 빼서 새로 리스트를 만든다고하면
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []
for item in fruits:
    if "a" in item:
        newlist.append(item)
print(newlist)

# list comprehension 을 사용하면 한 줄로 표현가능
newlist2 = [item for item in fruits if "a" in item]
print(newlist2)

# Syntax : newlist = [expression for item in iterable if condition == True]
newlist3 = [item for item in fruits]  # without condition
print(newlist3)


# set Comprehensions ---------------------------------------------
new_set = {item for item in range(5)} 
print(new_set)

# Dictionary Comprehensions --------------------------------------

new_dic = {item: item*2 for item in range(5)}  
print(new_dic)


# 궁금한점 : 아래와 같은경우 왜 새로만들어진 new_dic1 의 배열순서가 실행시마다 달라질까?
# ??? 새로 만들어진것든 set인데 set은 순서가 따로 없어서 그런걸까? 그렇다고해도 for 실행시 순서대로 iterate 하는것 아닌가?

a_dic = {"a":1, "b":2, "c":3, "d":4}
new_dic1 = {item for item in a_dic}
print(new_dic1)

# 아래의 경우는 실행할때마다 순서가 달라지는일 없슴
a_dic2 = {1:"james", 2:"colin", 3:"sara",4:"kevin"}
new_dic2 = {item for item in a_dic2}
print(new_dic2)

# 아래와 같이 list 의 경우에는 순서가 달라지지 않음
# 순서가 계속 바뀌는것은 iteable variable 이 set 또는 dictionary 이며, element가 int 가 아닌 string 인 경우인 듯 한데
# iterable 이 unordered 인 경우라는 설명이 있는데, 이것도 이해가 안가는게, dictinary 는 unordered --> ordered 로 바뀌었다고 하지 않았나?
a_dic3 = ["a", "b", "c", "d"]
new_dic3 = [item for item in a_dic3]
print(new_dic3)