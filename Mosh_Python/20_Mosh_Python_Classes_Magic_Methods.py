
# Magic methods are the methods which has double underscore at the front and end of the method names.
# __init__, __new__, __str__ etc.. so many of them.
# These magic methods are called automatically by python interpreter depending on how we use our object and classes.

# Below, we have a __init__ magic method. without calling this method, it is excuted when we create a new object from the class



class Phone:
    def __init__(self,year,model):
        self.release = year
        self.model = model
    
    def __str__(self):
        return f"{self.release} year, {self.model}"

    def what_do(self):
        print(self.release, self.model, ",I can call")

my_phone = Phone(2018,"iPhone XR")

my_phone.what_do()

print(my_phone) 
# when we execute, we can see this message: 
# <__main__.Phone object at 0x10bb37fd0> (name of the module / class name / memory address of the object)
# but we put this "def __str__(self):" in the class, we can make it return something when we print the object
 
# when we type "my_phone." we can see many magic methods available inherited from another object
