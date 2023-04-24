
# Comparing Objects

class City:
    def __init__(self,population,area):
        self.people = population
        self.scale = area

peterborough = City(90,"wide")
whitby = City(90,"wide")

print(peterborough == whitby)   # compare result: False
# We created two exactly the same object, but python says these two are different.
# it is because when compare something, python compares the address of the memory address

# to solve this problem, we can add a comparing method as below

class City2:
    def __init__(self,population,area):
        self.people = population
        self.scale = area

    # Python automatically calls the __eq__ method of a class when you use the == operator to compare the instances of the class
    def __eq__(self, other):
        return self.people == other.people # here, only compare "people" to determine if they are the same
        # if you wanna add more condition to determine if those instances are the same, you can use "and" "or" etc...
toronto = City2(90,"wide")
ajax = City2(90,"wide")

print(toronto == ajax) 
print(toronto.people)
print(toronto.scale)


print("===========================")
# another example -------

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, who):     # you can use any name instead of "another"
        return self.age == who.age and self.last_name == who.last_name   # compare two elements

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
print("another example: ", john == jane)




# another example -------
print("===========================")

class Person2:
    def __init__(self, first_name, last_name, age= 30): # age=30 is a default value, if there is no argument, using this default value
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Person2):
            return self.age == other.age

        return False


john = Person2('John', 'Doe', 25)
jane = Person2('Jane', 'Doe', 25)
mary = Person2('Mary', 'Doe', 27)

print(john == jane)  # True
print(john == mary)  # False


mark = Person2('Mark', 'Doe', 25)
print(mark == 20)  # False