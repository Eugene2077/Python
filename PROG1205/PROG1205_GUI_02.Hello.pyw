
# Change from hello.py to hello.pyw --> window app

# extension .pyw means windows applicaiton
from tkinter import *  # we need the widgets from tkinter to use GUI
# widgets(aka controls) are the buttons, label(text), textboxes(entries), comboboxes, etc

# replace the Tk widgets with the ttk ones(ttk looks more native, nicer)
from tkinter.ttk import *

from tkinter import messagebox
# when we import thinker above, every classes(frame, entry, button,, etc)are imported, but messagebox(pop up) is a module, so we have to import it manually


# functions

def click_greet():
    """Executed when the greet button is clicked"""
    name = input_text.get()  # get the value of the variable. "get" is a getter, if we don't use get, it passes just memory address
    if name:                 # if name is not blank
        messagebox.showinfo("Greetings!", f"Hello {name}")
    else:
        messagebox.showerror("Error", "Please enter your name")

def click_clear():
    """Excuted when the clear button is clicked"""
    # set the Entry text to an empty string
    input_text.set("")


# setup the window properties
# first of all, we need to create a new window
window = Tk()               # create new window
# TK is a framework that tkinter uses, tkinter is a python implementation of Tk
# and Tk is basically a widget mentioned above (the framework we are gonna use for the graphics)
window.title("Hello GUI World! - Eugene")  # set the title
window.iconbitmap("Hello.ico")             # change the window icon
window.resizable(width=False, height=False)   # set the window not resizable

# create a frame
frame = Frame()   # frame is an object from frame class(like as int, string, etc,.)
# frame is the area wehre all widgets are placed (not visible)

# Create a label (text)
# parameter(position,contents)
input_label = Label(frame, text="Please enter your name:")

# create a new entry (textbox)
# this is a tkinter variable, not a python variable, we store user input here
input_text = Variable()
# we can't store user's input at input-entry directly,
input_entry = Entry(frame, width=50, textvariable=input_text)  # Entry means input text box
# so we have to pass the input to the tkinter variable above

# create two buttons
# call the function you need to call
greet_button = Button(frame, text="Greet", width=12, command=click_greet) # command will connect the function to the button
clear_button = Button(frame, text="Clear", width=12, command=click_clear)

# position widgets on screen - using the function pack()
# parameter(frame has 10px padding, x and y each)
frame.pack(padx=10, pady=10)
input_label.pack(anchor="w")  # position of the label (w: west)
input_entry.pack()
# place the button to the right , padding of the button is 10px on the top side
greet_button.pack(side="right", pady=(10, 0))
clear_button.pack(side="left", pady=(10, 0))  # place the button to the left

# start the GUI : mainloop will keep redrawing the GUI
window.mainloop()
