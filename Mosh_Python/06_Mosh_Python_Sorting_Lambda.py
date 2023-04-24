 
# sorting the list  --------------------------------
number = [4,1,7,5]
number.sort()    # 정렬
print(number)
# reverse order
number.sort(reverse = True)  # 역순정렬

# 다른 방법도 있다, "solted" method 를 사용
sorted(number)               # sorted(iterable)  iterable에 어떤 iterable 가능한 것이라도 들어갈 수 있다
sorted(number,reverse=True)  # reverse order 반환
# 위 두가지 방법은 약간 다른 결과가 나오는데, 
#.sort() 는 원래의 variable 배열순서를 바꾸는데 반해, sorted()는 원래의 variable 은 그대로 두고 새로운 결과를 return 한다는 점


# 만약 tuple 로 이루어진 list 가 있다면
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]
items.sort()   # 이걸 sort() 하면
print(items)   # 이렇게는 sort 안됨(왜?),,, 이런경우는 function 을 하나 만들어야 한다

def sort_item(p):          # new function, 받아들이는 argument 에서  
    return p[1]            # index[1]을 반환
items.sort(key=sort_item)  # key= 는 사용자정의 function, 사용자정의함수(또는 python에 내장된 함수)를 사용하여 내용물을 정렬한다
print(items)


# Lambda Function --------------------------------
# 참고 : https://www.w3schools.com/python/python_lambda.asp
#  : 위에서처럼 새로운 function 을 정의할 필요없이 lambda function을 사용하여 아래와 같이 간략화하여 사용가능
items.sort(key=lambda item:item[1])  # lambda를 사용하면, 사용자정의 function을 여기처럼 간략하게 표현가능 (문법: Lambda parameters:expression)
# this is shorter and cleaner way to define function that we're going to use only once as an argument to another function.


# map function --------------------------------

# 상기 리스트(items)에서 product 는 관심없고, 오직 가격(숫자부분)만 뽑아서 list 로 만들려고 한다면
# 그래서 아래와 같이 원래의 list 를 다른 list 로 mapping 한다 (가격만 있는 list 로)
# for를 사용하는 경우
prices = []
for i in items:
    prices.append(i[1])
print(prices)

# 먼저 map() function 에 대해서 알아보면,,, 
# map() function syntax: map(function, iterables)
# The map() function executes a specified function for each item in an iterable. 
#The item is sent to the function as a parameter
def myfunction(p):
    return len(p)
x = map(myfunction,('apple', 'banana', 'cherry'))
# 이렇게 iterable 하게 매핑된 결과는 메모리에 저장된채로 x에는 저장된 메모리의 주소만 할당된다. 
# 이 매핑결과를 받아오기 위해서는 for 를 사용하여 해당결과를 출력하는 방법이 있고(저장된 것이 iterable 하기 때문에)
#또다른 방법은 아래처럼 casting 하는 방법이 있다
print(list(x)) # 맵핑후 그냥 출력은 안되고 리스트로 casting 해서 출력한다.

# map()에 user define function 을 사용하는 대신 Lambda function 을 사용하면
x1 = map(lambda p:p[1],items)  # p:parameter / p[1]: expression / items: iterable object
print(list(x1))
# 전체를 list 로 casting, 이러한 형태로 사용되므로 아래 문형을 잘 기억해 두자
x1 = list(map(lambda p:p[1],items))
print(x1)


# Rambda Function 을 사용한 filtering
items1 = [
    ("mouse", 8),
    ("power", 9),
    ("CDrom", 10),
    ("sound", 13)
]
# 위 list 에서 10 이상인 것만 추출한다고 하면
filtered = []
for i in items1:
    if i[1] >= 10:
        filtered.append(i)
print(filtered)

# 위와같이 해도 되지만, filter function 을 사용하면 더 간편하고 간결하다
# 기본문법: map() 과 동일 - filter(function, iterable)
filtered1 = filter(lambda p:p[1] >= 10, items1)
print(list(filtered1))
# 전체를 list로 casting, 이러한 형태로 많이 사용된다고 한다, 위 map()과, 여기 아래 filter()문형 둘다 잘 기억해 둘것
filtered1 = list(filter(lambda p:p[1] >= 10, items1))
print(filtered1)

# List Comprehensions: filterling 할때 아래와 같이 간결하게 해결가능, for loop 와 비슷한 이 문형은 원하는 것만 뽑아낼수 있다
# 문법 : [expression for i in items]
prices1 = [i[1] for i in items1]  # 위 items1 에서 가격부분만 따로 리스트로 만들어줌
print(prices1)  

# 위 87번줄에 있는것을 List Comprehension 으로 다시 쓴다고 하면
# we can use if statement here
filtered1 = [i for i in items1 if i[1] >= 10]
print(filtered1)