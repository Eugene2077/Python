
# in case of C language, it is compiled to machine code which is understandable for the computer
#whereas java is compliled to java bytecode running java virtual machine(JVM).   
# Similar to java, in case of Python(C python), it is compiled to Python Bytecode and running on 
#a Python Virtual Machine which will interprete ti to machine code. 

# There are variation in Python, Jathon(you can use java code), IronPython(You can use C#) and PyPy(Subset of pYthon)
# in case of Jathon, the Python(Jathon) code is compiled to Java Bytecode instead of Python Bytecode. 


# strings -----------

# quote inside of strings: use "" and '' to separate which is which
# use three quote(''' or """") for multiline strings
''' or """ also can be used to multiline comments since Python will 
ignore string literals that are not assigned to a variable '''

# variables -----------

from typing import ClassVar, ItemsView, TypeVar  # math module importing
import math
my_course = 'Python for Beginners'

# Naming convention:
# variables, objectives, methods, functions, package, module : lowercase with _(underscore)
# Constant : Uppercase with _
# Classes and class files: Pascal notation

# if you add index, it returns the chractor of the string.("-"from the last)
print(my_course[0])
# [-2] : the second letter from the end
# [0:5] : return index 0 ~ 4 (index 5는 제외됨에 주의: 항상 나중 index 위지의 letter 불포함)
# [:]  : string 전체
# [5:] : index 5부터 끝까지
# index number 에 space 도 포함

# formatted string : 아래 예에서 f(formatted string 을 사용한다는 명령어) 로 시작되는 string에서 {}를 사용하여
# 변수를 string안에 넣은것을 볼 수 있다.
# formatted string 을 사용함으로서 가독성을 좋게 할수 있다.
first = 'john'
last = 'smith'
message = f'{first} [{last}] is a coder'
print(message)

# String methods
print(len(my_course))     # len(built-in function): length of the string
print(my_course.upper())  # variable + dot 입력하면 javascript처럼 method 리스트 팝업
print(my_course.lower())  # 소문자로
print(my_course.title())  # 각 단어의 첫번째글자만 대문자로
print(my_course.strip())  # remove the white spaces both the beginning and the end of the string
print(my_course.lstrip()) # remove the white space the left side(beginning) of the string (뒤에것 제거는 rstrip)
print(my_course.find('yt')) # yt 의 index 값 반환
print(my_course.replace('P', 'Y'))
print("pro" in my_course) # "pro" 가 my_course 에 있는지 True or False 로 return
print("swift" not in my_course) # "swift"가 my_course 에 없는가? True or Flase

# Escape Sequences ---------
# next to the '\' will be ignored from syntax. it is called "escape sequences"
her_course = "Python \"programming\""
print(her_course)

# when you need to write in a new line, use '\n'
print("I wannna write this \nin a new line")


# Arithmetic Operation ---------

print(10 // 3)  # 나누기  소숫점 이하 무시 (floor)
print(10 % 3)   # modulus
print(10 ** 3)  # to the power of

x = 10
x += 3  # augment assignment operatorv: x = x + 3

# Math Functions -----------

x = -2.9
print(round(x))  # 반올림
print(abs(x))    # 절대값

math.ceil    # cealing of x : x 바로 다음에오는 정수 (x = 2.6 -> x cealing = 3)
math.floor   # floor or x : x 바로 이전에 오는 정수

# 기타 math functions : search with 'python math function'

# Casting
xxx = str(3)     # change to string
yyy = int(3.87)  # change to int (소수점이하 무시)
print(type(xxx))  # display the data type

# Booleans
print(bool('hello'))  # true
print(bool(12))      # True
print(bool([0, 1, 2]))  # True
print(10 > 9)        # True , 이런 조건식은 "bool" 명시하지 않아도 boolean 으로 출력
# most value is equivlant to True if it has any content, except belows
bool('')      # False
bool(0)       # False
bool([])      # False
bool({})      # False
bool()        # False
bool(None)    # False
bool(False)   # False
bool("False") # True

# Boolean using in function

def my_function():   # function 에서 True 를 반환하고
    return True

if my_function():    # 원래 my_function() = True 이지만 이렇게 생략해서 씀
    print("yes it is")
else:
    print("no")

x = 200
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
print(isinstance(x, int))
# 이런식으로 표현도 가능, 세개중 하나에 해당하는가의 답을 boolean 으로 반환
print(isinstance('hello', (int, str, bool)))







