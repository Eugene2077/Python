
# Bonus ICE 3
# File name : HSTcalculator.pyw

# Name: Hongju(Eugene) Shin
# Date: November 28, 2021
# App Name: HST calculator
# Description: This app will calculate the HST of a given dollar amount

# import widgets from tminter
from tkinter import *
# replace the Tk widgets with the ttk
from tkinter.ttk import *

# constant
HST = 1.13


# functions
def calculate_click():
    """Executed when the calculate button is clicked"""
    input_value = input_text.get()  # get the value of the variable.

    # if the user input '$', it is still valid but we need ignore this letter
    input_value = input_value.replace("$","")

    # validation for numeric value (float)
    try:
        input_value = float(input_value)
        numeric = True              # if it is succesful
    except:
        numeric = False             # if it is unable

    # if it is not successful
    if not numeric:
        # setter method will set the value of the variable
        output_text.set("Error - Please input a dollar amount in a number!!")
    elif input_value <= 0:
        # setter method will set the value of the variable
        output_text.set("Error - Negative dollar amount is not acceptable!!")

    # when it is valid number, calculate the output and diaplay it
    else:
        output_text.set("$",round(input_value * HST, 2))



def clear_click():
    """Excuted when the clear button is clicked"""
    input_text.set("")     # set the input_value to an empty
    output_text.set("")    # set the output_value to an empty


# setup the window

window = Tk()                                # create new window
window.title("HST Calculator - Eugene")      # set the title
window.iconbitmap("cash.ico")                # change the window icon
window.resizable(width=False, height=False)  # set the window not resizable

# create a frame
frame = Frame()

# Create a labels
input_label = Label(frame, text="Enter a dollar amount:")
output_label = Label(frame, text="Amount + HST: ")

# Entries
input_text = Variable()    # a tkinter variable for GUI
input_entry = Entry(frame, width=60, textvariable=input_text)  # textvariable links the entry with the variable
output_text = Variable()   # a tkinter variable for GUI
output_entry = Entry(frame, width=60, state="readonly", textvariable=output_text)

# Buttons
calculate_button = Button(frame, text="Calculate", command=calculate_click)
clear_button = Button(frame, text="Clear", command=clear_click)

# position widgets on screen - using the function pack()
# parameter(frame has 10px padding, x and y each)
frame.pack(padx=10, pady=10)
input_label.pack(anchor="w")        # position of the label (w: west)
input_entry.pack(pady=(0, 10))
output_label.pack(anchor="w")       # position of the label (w: west)
output_entry.pack(pady=(0, 10))
calculate_button.pack(side="right")  # button to the right
clear_button.pack(side="left")      # button to the left

# Keyboard binding
window.bind('<Return>', lambda event: calculate_click())  # Return key, bind to calculate_click function 
window.bind('<Escape>', lambda event: clear_click())      # Escape key, bind to clear_click function 

# mainloop will keep redrawing the GUI
window.mainloop()
