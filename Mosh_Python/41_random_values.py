from random import randint, random, choice, choices, shuffle
import string

print(random())
print(randint(1,1000))
print(choice([1,2,3,4,5]))
print(choices([1,2,3,4,5], k=3))
print(choices(["ds","asd","ek","gr"], k=3))
print(choices("abcdefghi", k=5))
print("".join(choices("abcdefghi", k=4)))
print(",".join(choices("abcdefghi", k=4)))

print(string.ascii_letters)
print(string.digits)
print("".join(choices(string.ascii_letters + string.digits, k=10)))    # random password 만들때 등 사용

# shuffle
number = [1,2,3,4]
shuffle(number)
print(number)