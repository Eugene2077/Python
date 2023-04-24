# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# python 3.7부터 Dictionary 가 unordered --> ordered 로 변경됨

# Dictionary 는 아래와 같이 key part 와 value part  로 구성된다. 
point = {"x": 1, "y": 2}   # 여기서 key는 string "x", value 는 int 1 로 사용한 예
# key 는 반드시 immutable type(그 type이 변할수없는 변수) 이어야 한다 (int, float, decimal, bool, string, tuple, and range)
# 참고 mutable data type (list, dictionary, set, and user-define classes)

# we can declare a dictionary using a keyword argument
point = dict(x = 3, y = 4)    # 결과: {"x": 3, "y": 4}

# we can access the values using key instead of index (인덱스 사용하는것과 동일하게 key 사용)
print(point["y"])   # {"x": 3, "y": 4}

point["x"] = 3.5    # key["x"] value 변경   {"x": 3.5, "y": 4}
point["z"] = 7      # 새로운 값 추가          {"x": 3.5, "y": 4, "z": 7}
del point["x"]      # "x" 값 삭제 
print(point)

# 먄약에 없는 key 값을 찾으려고 한다면 에러가 발생하는데, 이런 에러를 피하려고 한다면 아래와 같은 방법을 쓰면 된다
# print(point["a"])     # 이렇게 실행하면 에러 발생
if "a" in point:        # 해당 item 이 없을때 에러발생을 피하기 위함
    print(point["a"])
point.get("a")          # 또는 이렇게 get이라는 method 를 사용할 수 있고, 데이터가 없는경우 None를 return 한다.
# get 을 사용하는경우  point.get("a", 0) 이렇게 쓰면 해당 item 없는경우 None 대신 0을 return 한다.

# loop over dictionary -------------------------------------------
for item in point:   # dictionary 역시 iterable 이기 때문에 loop 가능
    print(item)      # iteration 되는것은 key 이기 때문에 : y, z 등의 key 만 출력된다.
    print(item, point[item])  # y 4 이런식으로 key 와 value 둘 다 출력.

# 다른방법의 loop 도 있다.
for item in point.items():
    print(item)      # ("y", 4) 이런식으로 key와 value를  tuple 로 출력
# 또는 이런식으로 한다면
for item, item2 in point.items():
    print(item, item2)  # y 4 이런식으로 위에 위에 것과 동일한 결과

