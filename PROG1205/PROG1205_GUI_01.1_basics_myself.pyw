

from tkinter import *  # we need the widgets from tkinter to use GUI
from tkinter.ttk import *


root = Tk()               # create a new object, name doesn't matter(it is only a variable - 'root' or 'windows' waatever
root.title("Hello GUI World! - Eugene")  # set the title
root.iconbitmap("cash.ico")
  

# Frame()
# A frame in Tk lets you organize and group widgets. It works like a container. 
# Its a rectangular area in which widges can be placed.
my_frame = Frame()   




# buttons
# Parameters(master,option)/ master: the parent window , option: 참고 https://www.tutorialspoint.com/python/tk_button.htm
button01 = Button(my_frame, text="button 1")







# pack()
# Layout Managers: we use "pack()"" here
# Tkinter has three Layout Managers that use geometric methods to position widgets 
# -in an application frame: pack, place, grid
# pack is the easiest Layout Manager to code with in Tkinter.
# Instead of declaring the precise location of a widget, the pack() method declares the 
# -position of widgets in relation to each other. However, pack() is limited in precision 
# -compared to place() and grid() which feature absolute positioning. 
# For simple positioning of widgets vertically or horizontally in relation to each other, 
# -pack() is the Layout Manager of choice."""
my_frame.pack(padx = 10, pady = 10)






# app 이 계속 refresh 상태로 있게해줌
root.mainloop()
