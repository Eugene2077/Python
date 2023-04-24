from tkinter import *
from tkinter.ttk import *

root = Tk()

my_label_1 = Label(root, text= "Hey, howdy?")
my_label_2 = Label(root, text= "My name is John Elder")



frame = Frame()
frame.pack(padx = 10, pady = 10)

my_label_1.pack(anchor=SW)
my_label_2.pack(anchor=NE)

root.mainloop()
