

values = [x * 2 for x in range(10)]
for x in values:
    print(x)

# 만약에 values 에 대단히 많은 데이터가 들어간다면 이 모든 data 를 여기에 넣어서 과도한 메모리 소모를 할 필요가 없다.
# 이러한 경우 generator 를 사용하여 iterating 하는것이 좋다. 

# 아래와 같이 ()안에 comprehension 을 넣으면 generator 가 된다. 
# Tuple comprehension은 python에서 사용하지 않으니 혼동하지 않아도 된다. 
value2 = (x * 2 for x in range(1000000))
for x in values:
    print(x)
# 여기서 만약 range 가 굉장히 큰 숫자라고 해도, 전혀 메모리가 증가하지 않는다. (그냥 generator로 저장되기 때문에)
