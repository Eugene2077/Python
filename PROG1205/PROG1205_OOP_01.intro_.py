# Class 설명 from the PROG1205 - Fred
# Class name : PascalCase 사용
# Object name : snake_case 사용
# 통상 class 마다 별개의 파일로 작성함: 유지관리의 편의/ class name: PascalCase 사용

# Function / Method : Class 내에 있으면 method, class 바깥에 있으면 function
# Function / Method : snake_case 사용


from PROG1205_OOP_intro_Class_Student import StudentNew
from PROG1205_OOP_intro_Class_Student import Student


def greeting(name:str):
    """this function is only for practice, do nothing"""
    print("hello,",name)
    # 본 예제에서 name은 parameter name, str 은 data type에 관한 documentation, 
    #이런식으로 작성하면 함수호출할때 괄호를열면 어떤 데이터 type를 넣어야하는지 알려줘서 편리함
    # 그리고 """"""은 function 사용시 괄호를 열면 안내가 나오도록 함(co working 등에서 유용함)

# calling the function
greeting("fred")

# python 에서는 return 값이 있건 없건간에 function 이름앞에 void 또는 int 등을 넣을 필요가 없다
#(다른 언어에서는 void(리턴없슴), int(정수 리턴) 등 접두사가 들어가잖아)
# function 실행중 return 이 나오면 실행을 즉시 중단하고 해당값을 return 한다.

# ----------------- 예제

# 본 예제에서는 (PROG1205_OOP_intro_Class_Student.py) 라는 별도의 파일을 class 파일로 만듬
# 위 student 파일을 사용하는 법:

# class 이름인 Student() 타이핑하다보면 자동으로 위 from ~ import 라인추가할수있는 snipet 나옴
# 위 from ~ import 에서 import 다음에 * 을 넣어서 해당 문서의 모든 class 를 import 할 수 있슴
fred = Student() # Creating an object named "fred"

# object "fred":아래 fred 를 타이핑하고 .을 타이핑하면 snippet 에서 해당 class 로부터 이 object로 상속된 property를 쓸 수 있슴
fred.name = "fred"
fred.program = "physics"
 
print(fred.name)
print(fred.program)
print(fred.get_name())

fred.set_name("Jason")       # using the setter
print("new",fred.get_name()) # using the getter

fred.set_program("Literature")
print("new",fred.get_program())


# 위와같이 name 과 program 을 따로 정의하지않고 object 를 만들때 한번에 정의히기 (Python 에서만 제공하는 기능이다)
john = StudentNew("John Nash","Mathmatic")

print(john.get_name())
print(john.get_program())

john.set_name("John Cusak")
john.set_program("Filming")

print(john.get_name())
print(john.get_program())


maya = StudentNew("Maya Madison","History")
print(maya.name, maya.program)

print("--------------")

# function 을 이용: object 로부터 원하는 정보를 빼서 출력하는 function
def print_information(student:StudentNew):
    # student: parameter, StudentNew: class(어떤 클래스의 입력인지 말해주는것으로 마치 int, str 등과 같은 역할은 하는 것이다.)
    """this function receives a student object and print their name and program"""
    print(student.get_name())
    print(student.get_program())

print_information(maya)