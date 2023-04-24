class Student:
    # internal variables
    name:str
    program:str

    # getter (accessor)
    def get_name(self): # defining a method 
        """gets the student's name"""
        # a method in python has this (self)keyword (only in python)
        # "self" means the class (like as 'this' in Javascript?)
        return self.name # return the 'name' in this class
    
    def get_program(self):
        """get the student's program"""
        return self.program

    # setter (mutator)
    def set_name(self, name:str):
        """set the student's new name"""
        self.name = name
        # 위 예에서 (self, name:srt) 에 들어간 name 은 그 아래줄 self.name 에 들어간 name 과는 다른것이다. 
        #윗줄 name 은 set 을 위해서 이 method 내에서만 사용되는 변수인데 반해, 아래줄의 name 은 이 method 가 속한 class내에서 사용되는 name 변수임.

    def set_program(self, program:str):
        """set the student's new name"""
        self.program = program
        


class StudentNew:
    name:str
    program:str
    # 위와같이 name 과 program 을 따로 정의하지않고 object 를 만들때 한번에 정의히기 위해서는 아래 constructor가 필요하다
    # it is weird but, constructor in python looks like this
    def __init__(self, name:str, program:str):
        """build new student based on their name and program"""
        self.name = name
        self.program = program

    def get_name(self):
        return self.name
    def get_program(self):
        return self.program

    def set_name(self, name:str):
        self.name = name
    def set_program(self, program:str):
        self.program = program

