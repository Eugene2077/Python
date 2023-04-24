
# Instance vs Class Methods
# There are three types of methods in Python: instance methods, static methods, and class methods.

# ** Decorators **
# Decorators are simply functions, You can write them yourself, or use those included in libraries, or the Python standard library.
# Like any function, decorators perform a task. The difference here is that decorators apply logic or change the behavior of other functions. They are an excellent way to reuse code, and can help to separate logic into individual concerns.
# a decorator, it is kind of function but it doesn't need"()" unless you are passing in arguments.

# --  instance methods --
# The most common method type. Able to access data and properties unique to each instance.
# Instance method must have "self" as a parameter, but you don't need to pass this in everytime. 
# inside any instance method, you can use "self" to access any data or methods that may reside in your class. "self" is the only way to access them.
# Instance methods are the most common, there's no decorator needed. Any method you create will considered as an instance method

# -- Static Methods --
# Cannot access anything else in the class. Totally self-contained code.
# Static methods are methods that are related to a class in some way, but don't need to access any class-specific data.
# You don't have to use self, and you don't even need to instantiate an instance, you can simply call your method:
# Static methods are great for utility functions, which perform a task in isolation. They don't need to (and cannot) access class data.

# -- Class Methods --
# Can access limited methods in the class. Can modify class specific details.
# Class methods can't access specific instance data, but they can call other static methods.
# Class methods don't need "self" as an argument, but they do need a parameter called "cls". This stands for class, and like self, gets automatically passed in by Python.
# 이건 뭐하는데 쓰는걸까 하겠지만, 나름대로 용도가 있다: Class methods can manipulate the class itself, which is useful when you're working on larger, more complex projects.
# 즉, 클래스에서 정의된 기본 오브젝트와 속성이 조금 다른 오브젝트를 형성하고자 할때, 물론 passing 되는 arguments 를 다르게 해서 오브젝트를 형성할 수도 있지만 class method 를 사용하여 passing 되는 argument 자체를 다양하게 사용할 수 있다.



from datetime import date
  
class Person:                           # 
    def __init__(self, name, age):      # an instance method
        self.name = name                # self 를 사용하면 파생된 모든 objects 에 적용된다
        self.age = age
      
    # a class method to create a Person object by birth year. object를 만들때 경우에 따라 만약에 나이 대신 출생년도를 argument로 넘겨주고 싶을대 이렇게 class method 를 사용하여 연산을 행한 뒤에 이 클래스에서 사용되는 argument로 다시 넘겨줌
    @classmethod
    def fromBirthYear(cls, name, year):  # "self" 대신에 "cls" 를 사용한다
        return cls(name, date.today().year - year)   # 연산후 그 결과를 이 class 내에서 해당되는 parameter 로 사용함
      
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
  
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
  
print (person1.age)
print (person2.age)
  
# print the result
print (Person.isAdult(22))



print("===================================================")