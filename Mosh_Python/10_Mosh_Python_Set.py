
# Sets are used to store multiple items in a single variable
# unordered, unchangeable(remove or add 가능), and unindexed. 
# 그리고 같은 item 의 중복을 허용안함 (순서가 없으니 중복마저 허용한다면 구분이 안될것같네)

numbers = [1,1,2,3,4,4]  # let say we have a list : there are the same elements in the list
first = set(numbers)     # 이렇게 set으로 casting 하면 중복된 엘리먼트는 하나씩만 남기게 됨 : 왜냐하면 set에서는 중복을 허용 X
print(first)             # {1,2,3,4} 출력

second = {0,1,2}      # a set
second.add(5)       # add an element
second.remove(5)    # remove an element
len(second)         # number of element

first | second      # union : 두 셋의 합집합
first & second      # intersection : 두 셋의 교집합
first - second      # intersection : 빼기
first ^ second      # intersection : 두 셋중 어느 하나에만 속하는것만(합집합-교집합) : {0,3,4}

# set 은 순서가 따로 없다, 그러므로 index[]를 사용할 수 없다.

if 1 in first:      # 뭐가 안에 있는지 보려면 대충 이런식으로...
    print("yes")
