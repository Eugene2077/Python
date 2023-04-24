





from tkinter import *
from tkinter.ttk import *

# Def






# keyboard binding
def key_handler(event:Event):
    """Function that handles key presses
    [Enter] : convert
    [Esc] : clear_entries
    """
    if event.keysym == "Escape":     # esc key to clear function
        clear_entries()
    elif event.keysym == "Return":   # return key to convert function
        convert()



# setup window
window = Tk()                                        # creat a new window
window.title("Temperature Switch - Lauren Risden")   # set the title
window.iconbitmap("temp.ico")                        # change the window icon
window.minsize(width=360, height=300)                # set minimum size of the window 
window.bind("<Key>", key_handler)                 

# Frames
frame = Frame()
input_frame = Frame()
radiobutton = LabelFrame(text= "Please insert a conversion: ")
output_frame = Frame()

# Label
enter_number_label = Label(output_frame, text="")
result_label = Label(output_frame, text="")

# Radio button
convert = Variable()
celsius_farenheit = Radiobutton()
farenheit_censius = Radiobutton()

# Buttons
convert_button = Button(input_frame)
restart_button = Button(input_frame)

# Place the widgets in Pack()
frame.pack(padx=10, pady=10)
input_frame.pack()
radiobutton.pack()
output_frame.pack()



window.mainloop()