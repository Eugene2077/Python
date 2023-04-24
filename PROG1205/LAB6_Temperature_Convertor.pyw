
# Name : 
# Date : 
# App Name : Temperature Convertor
# App Description: App that convert the temperature units

from tkinter import *
# replace the Tk widgets
from tkinter.ttk import *
# import messagebox
from tkinter import messagebox


# Functions

def convert():
    """Excuted when the convert button is clicked"""
    temp = input_text.get()           

    try:
        temp = float(temp)
    except:    # not valid error display
        output_text.set("Not numeric!, Please input temperature in numeric")

    if option.get() == "cels":          

        result = (temp-32) * 5/9
        output_text.set(f"{result:.1f}°C")   
        input_text.set(f"{temp}°F")         

    elif option.get() == "fere":      
        # calculate to fahrenheit
        # fomula for converting to fahrenheit
        result = (temp * 9/5) + 32
        # round output to 1 decimal point
        output_text.set(f"{result:.1f} °F")
        input_text.set(f"{temp} °C")      


def reset_entry():
    """Excuted when the clear button is clicked"""
 
    input_text.set("")   
    option.set("cels")  
    output_text.set("")      

# keyboard binding
def key_handler(event:Event):
    """Function that handles key presses
    [Enter] : convert
    [Esc] : reset_entry
    """
    if event.keysym == "Escape":     # esc key to clear function
        reset_entry()
    elif event.keysym == "Return":   # return key to convert function
        convert()


# set up the window
window = Tk()     # creat a new window
window.title("Temperature convertor - Cailan") # set the title

window.resizable(width=False, height=False)    # set the window not resizable
window.bind("<Key>", key_handler)              # <key> : when the key is pressed, it execute a function 

# create a frame
frame = Frame()

# Create a labels
input_label = Label(frame, text="Enter the temperature you want to convert :")
output_label = Label(frame, text="Convertion result is: ")

# Entries
input_text = Variable()    # a tkinter variable for GUI
# textvariable links the entry with the variable
input_entry = Entry(frame, width=55, textvariable=input_text)

output_text = Variable()   # a tkinter variable for GUI
output_entry = Entry(frame, width=55, state="readonly",
                     textvariable=output_text)

# radio buttons
option = Variable()  # variable used in the radiobutton
radiobutton_celsius = Radiobutton(
    frame, text="Convert to Celsius", variable=option, value="cels")
radiobutton_fahrenheit = Radiobutton(
    frame, text="Convert to Fahrenheit", variable=option, value="fere")
option.set("cels")

# Buttons
button_convert = Button(frame, text="Convert", command=convert)
button_clear = Button(frame, text="Clear", command=reset_entry)

# position widgets on screen - using the function pack()
# parameter(frame has 10px padding, x and y each)
frame.pack(padx=10, pady=10)
input_label.pack(anchor="w")        # position of the label (w: west)
input_entry.pack(pady=(0, 10))

radiobutton_celsius.pack(anchor="w")
radiobutton_fahrenheit.pack(anchor="w")

# position of the label (w: west)
output_label.pack(anchor="w", pady=(5, 0))
output_entry.pack(pady=(0, 10))
button_convert.pack(side="right")  # button to the right
button_clear.pack(side="left")     # button to the left


# make the window visual
window.mainloop()
