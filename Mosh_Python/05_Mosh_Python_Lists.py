# list elements : string, number, boolean or others can be elements of list

from typing import ItemsView


letters = ["a", "b", "c"]
# it is a multi-dimensional list, 3차원인가(?)
matrix = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
if_we_need_100_of_zeros = [0]*100
print(if_we_need_100_of_zeros)

# we can use + to concatenate multiful lists
combined = letters + matrix
print(combined)

# list() function : make a list using something iterable
long_list = list(range(30))   # make a list using range function
print(long_list)

# iterating the strings include the spaces
long_list2 = list("a string is also iterable")
print(long_list2)


# Accessing items --------------------------------
characters = ["a", "b", "c", "d"]
characters[0]        # retern "a"
characters[0] = "A"  # modification
characters[0:3]      # index 0~2 까지
characters[0:]       # from index 0 to the end
characters[:]        # select all
characters[::2]      # step: every second(or third.. forth) elements

number = list(range(10))
print(number[::2])   # 짝수만
print(number[::-1])  # 역순으로


# Unpacking  --------------------------------
numbers = [1,2,3]               # there is a list
first, second, third = numbers  # unpack the list to each variables
print(first,second,third)       
# 주의할점: the number of elements in the list == the number of variables, 
# 갯수가 일치하지 않으면 에러발생하는데, 만약 처음부터 두개만 필요한 경우 아래와 같이 한다
first, second, *third = numbers  # 이렇게 *을 사용하여 나머지것들은 모두 third 변수에 저장, 이렇게 여러개의 element를 
#하나로 묶는것을 packing 이라고 하며 unpacking과 반대의 개념, python 에서는 packing 할때 *을 사용하여 간편하게 수행하며
#앞에 function 에서 불특정한 수량의 argument를 받을 때 *을 사용하여 tuple 로 packing 한 것도 동일한 개념임

first, *second, third = numbers  # 이 경우 첫번째와 마지막 element만을 변수로 저장, 중간 나머지는 모두 second에 packing


# looping over list  --------------------------------
the_list = ["a","b","c"]      # a list
for item in enumerate(the_list):   # enumerate() : return the index and the element as a tuple at each iteration,
    print(item)                    # (0,'a') 이런식으로 각 iteration 마다 index 와 element 를 tuple 로 반환함
     
for item, item2 in enumerate(the_list):  # enumerate() 를 사용하여 각 iteration 마다 tuple((0,"a")이런식으로) 로 반환되는것을
    print(item,item2)                    #다시 한번 unpack 하여 tuple 이 아닌 그냥 index 와 element로 분리


# Adding items  --------------------------------
letters = ["a","b","c"]
letters.append("d")      # 뒤에 d 삽입
print(letters)
letters.insert(0,"z")    # index 0에 z 삽입
print(letters)


# Removing items  --------------------------------
letters = ["a","b","c","d","e","f"]
letters.pop()       # 마지막 element delete, you can put an index number in ()
print(letters)
letters.remove("b") # delete "b" (if there are more than one, remove the first one), if you wanna delete all "b", use loop
print(letters)
del letters[0:2]    # delete index[0]~ before[2]
print(letters)
letters.clear()     # delete all


# Finding items  --------------------------------
letters = ["a","b","c","d","f","c"]
print(letters.index("b",0,3))   # find the index of "b" between 0 ~ 3
# 만약 찾지 못한경우 댜른 언어에서는 -1을 반환(c)하는데비해 python 에서는 error가 발생한다, 이런 에러를 방지하기 위해서는 아래와 같이 하면됨
if "d" in letters:
    print(letters.index("d"))

# 동일한 item이 몆번 나오는지 알고싶을때는 
print(letters.count("c"))


 