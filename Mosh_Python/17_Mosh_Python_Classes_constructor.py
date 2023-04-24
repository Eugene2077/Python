
class Point:
    # __init__() method indicate that Python will use the method internally. In other words, you should not explicitly call this method.
    # Since Python will automatically call the __init__() method immediately after creating a new object, you can use the __init__() method to initialize the object’s attributes.
    # self: a reference to the current object. Javascript의 this 와 동일하지만, python 에서는 관행상 "self"라고 하는것이고 이름은 뭐가됐든 첫번째 parameter가 그 역할을 한다.
    # optionally, we can add any additional parameters for initiallizing(아래 a,b)
    def __init__(self, a, b):    # a,b : parameters
        self.a = a               # use "self" to define attribute of the object 
        self.b = b

    def draw(self):
        print("draw")

new_object = Point(1,2)          # create a new object with passing the arguments(1,2)
print(new_object.b)


# * Mosh 는 __init__ 를 constructor 라고 하는데, 아래 웹사이트에 의하면 constructor가 아니라고 함
# Note that the __init__ method doesn’t create the object but only initializes the object’s attributes. Hence, the __init__() is not a constructor.
# https://www.pythontutorial.net/python-oop/python-__init__/





print("-----------------------------------------------------")
print('기능을 이해하기 위한 연습')

class Point2:
    def draw(self):
        print("okay, then")
    def draw2(self,x,y):
        print("let's print this printed material")
        self.a = x
        self.b = y
        
p2 = Point2()
p2.draw()
p2.draw2(1,2)

print(p2.a, p2.b)


print('')
print("-----------------------------------------------------")




class Car:
    def __init__(self,year,model):
        self.produced_year = year
        self.model_name = model
    def output(self):
        print("year =", self.produced_year)
        print("model =", self.model_name)
        
my_car = Car(2017,"murano")
print(my_car.produced_year)
print(my_car.model_name)
my_car.output()

print('')
print("-----------------------------------------------------")

class Human:
    def __init__(self,age,sex,name):
        self.age = age
        self.sex = sex
        self.name = name

    def what_can(self):
        print("I can speak")

    def who_you(self):
        print("my age is",self.age)
        print("I am a",self.sex)
        print("my name is",self.name)

minsu = Human(48,"man","Kim Min Su")
print(minsu.name)
minsu.what_can()
minsu.who_you()