

# instance attribute : 오브젝트를 형성할 때 아래 sqft,price 처럼 argument로 넘겨받아 object마다 필요에 따라 다른 속성으로 만들어지는 attribute를 지칭한다.
# class attribute : class 내에서 속성이 지정되어 모든 오브젝트에 동일하게 적용되는 속성을 말한다.


class House():
    def __init__(self,sqft,price):
        self.area = sqft      # an instance attribute (여기서 정의된 속성은 생성된 모든 object에 적용)
        self.value = price    # instance attribute 
    def listing(self):
        print(f"the area is {self.area}sqft and the price is ${self.value}")

    basement = True     # a class attribute (applied to all the object as the same in here)
    garage = True       # a class attribute

his_house = House(2000,100000)  # creating an object   
print(his_house.area)           # print an attribute in the object
print(his_house.value)
his_house.listing()             # call a method in the object

print(his_house.basement)       # print an attribute in the object (this attibute is defined in the Class)
print(his_house.garage)


# we can add another attributes to the generated object 
his_house.rooms = 5   # add a new intance attribute (만들어진 instance에 속성을 변경)
his_house.rooms = 6   # change the attribute
print(his_house.rooms)

# we can also change or add new attribute in the class
House.basement = False
House.garage = 2
House.rooftop = True   # add a new attribute in the class
# 이렇게 클래스의 속성을 변경하면 이후 만들어지는 object 뿐 아니라 이미 만들어진 object의 속성도 따라서 변하게 된다.
print(his_house.basement)      
print(his_house.garage)
print(his_house.rooftop)

