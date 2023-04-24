

numbers = [1,2]    # there is a list
# when we type dot after the object (numbers.), we can see every methods in the object

# class is like a blueprint for creating new objects'
# an object is an instance of a class


# Creating a custom class ------------------------------------

class MyPoint:          # class uses pascal notation
    def draw(self):     # define a function, all function in a class shuld have at least one parameter
        print("draw")

point = MyPoint()       # creating an object       
point.draw()            # point. 을 타이핑하면 MyPoint class 에 만들어 놓은 draw method 을 선택할 수 있슴

print(type(point))      # 확인해보면 point 의 type 은 MyPoint class 임을 알 수 있다
print(isinstance(point, MyPoint))   # point 가 class MyPoint 의 instance 인가? 답은 True
print(isinstance(point, int))       # point 가 class int 의 instance 인가? 답은 False