

# what if we wanna print indivisual items in a list
numbers = [1,2,3]
print(*numbers)    # * 는 javascript의 ...(spread) 와 같은 역할을 한다. 각각의 item 을 별도로 출력

a,*b = numbers     # unpack, 첫번째것 첫번째에넣고, 나머지는 두번째에
print(a,b)

numbers2 = list(range(5)) # 0~4 까지의 list 를 만듬
print(*numbers2)

numbers3 = [*range(6)]    # 0~5까지의 list를 만듬
print(numbers3)

numbers4 = [*"hello ya"]    # string을 분해, list를 만듬
print(numbers4)