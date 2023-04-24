print(" for loop ----------------------------------------- ")

# 기본문법
for item in 'Python':               # string 을 이용한 loop
    print(item)
for item in [1, 2, 'three', True]:  # List 를 이용한 loop
    print(item)
for item in range(5, 10, 2):        # 범위지정, 5~9까지 2씩증가
    print(item)

print(" else ------------ ")

# else 의 사용법: loop가 break 없이 정상적으로 모두 종료되엇을 때 else 가 작동한다.
for n in range(2,10):       # 2~20 까지 loop (마지막 숫자인 20은 제외됨에 주의)
    for x in range(2,n):    # nested loop
        if n % x == 0:      # n 이 x 로 나머지없이 나누어 떨어지면, 약수가 있다는 뜻 (소수가 아니라는..)
            print(n, 'equals', x, '*', n/x)    # 뭘로 나누어 떨어지는지 보여줌
            break                              # 일단 약수가 발견되면 더 찾아볼것 없이 break
    else:   # 약수가 발견되지 않은채로 검색 끝냈으면 else 실행
        print(f"{n} is a prime number")

# when we test what the type of "range" is
print(type(range(5)))  # display 'class 'range''
# in python there are primative types  and complex types, 'range' is one of the complex types
# what is interesting about this 'range' object is, it is an iterable so, we can use it in 'for'
# iterable objects: strings, lists, tuples, dictionaries, sets


print(" while loop ----------------------------------------- ")

# while is not iterating over iterable object, it is evaluate the condition and repeating the task
number = 100        # 임의의 숫자
while number > 0:   # 조건식, 숫자가 0보다 크다면 계속 루프
    print(number)   # 
    number //= 2    # 정수나눔(소숫점은 모두 버림) ( a = a // 2 와 동일)

# else: loop 가 break 없이 정상적으로 모두 종료되어 더 이상 조건이 true 가 아닌경우 실행
# continue : stop the current iteration and continue with the next



