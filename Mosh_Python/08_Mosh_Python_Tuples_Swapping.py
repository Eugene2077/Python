
# Tuples -----------------------------------
# tuple is a read only list, we can't modify, add or remove 
point = 1, 2           # Tuple 에는 ()를 사용하지만, 아무것도 없고 단지 element뒤에 (,)가 나오는 경우
print(type(point))     #it is consider a tuple
point1 = (1,2) + (3,4) # concatenate is possible
point2 = (1,2) * 3     # multiplication is possible
sum = point + point1 + point2
print(sum)
point3 = tuple([1,2])  # Casting to a tuple, tuple(iterable)


# Swapping -----------------------------------
x = 10
y = 11
x, y = y, x      # python 에서는 이렇게 간편하게 값을 바꿀 수 있다.
x, y = (11, 10)  # python 내부에서 실제로 벌어지는 일은 이렇게 진행된다. y, x 값을 tuple 로 변환한 다음 unpacking 