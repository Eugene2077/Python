
# Name : Hongju (Eugene) Shin
# Date : 05 Dec 2021
# App Name : Caesar Cipher
# App Description: App that encript and decript the message from user's input

# import widgets from tminter
from tkinter import *
# replace the Tk widgets with the ttk
from tkinter.ttk import *
# import messagebox
from tkinter import messagebox

# Constant
ENCRIPTION_KEY = 200

# Functions


def encrip_decrip():
    """Excuted when the execute button is clicked"""
    if option.get() == "Encript":          # if the option is "Encription"
        message = input_text.get()         # get the input text
        # define an empty variable for the encripted message
        encrypted_message = ""
        for letter in message:             # Encrypt the letter by getting its numeric value and adding the ENCRYPTION_KEY
            encrypted_message += chr(ord(letter) + ENCRIPTION_KEY)
        output_text.set(encrypted_message)  # display the encripted message

    elif option.get() == "Decript":        # if the option is "Decription"
        message = input_text.get()         # get the input text(encripted message)
        # define an empty variable for the encripted message
        decrypted_message = ""
        for letter in message:             # Encrypt the letter by getting its numeric value and subtracting the ENCRYPTION_KEY
            decrypted_message += chr(ord(letter) - ENCRIPTION_KEY)
        output_text.set(decrypted_message)  # display the encripted message

    else:     # nothing is selected, pop up a messagebox
        messagebox.showwarning(
            "No Selection!", "Please select one: Encription / Decripton!")


def clear_entries():
    """Excuted when the clear button is clicked"""
    input_text.set("")     # set the input_value to an empty
    output_text.set("")    # set the output_value to an empty


# set up the window
window = Tk()     # creat a new window
window.title("Caesar Ciper - Eugene")              # set the title
window.iconbitmap("lock1.ico")              # change the window icon
window.resizable(width=False, height=False)  # set the window not resizable

# create a frame
frame = Frame()

# Create a labels
input_label = Label(frame, text="Enter your message or code:")
output_label = Label(frame, text="Encripted/Decripted text is: ")

# Entries
input_text = Variable()    # a tkinter variable for GUI
# textvariable links the entry with the variable
input_entry = Entry(frame, width=70, textvariable=input_text)

output_text = Variable()   # a tkinter variable for GUI
output_entry = Entry(frame, width=70, state="readonly",
                     textvariable=output_text)

# radio buttons
option = Variable()  # variable used in the radiobutton
radiobutton_encript = Radiobutton(
    frame, text="Encription", variable=option, value="Encript")
radiobutton_decript = Radiobutton(
    frame, text="Decription", variable=option, value="Decript")

# Buttons
button_execute = Button(frame, text="Execute", command=encrip_decrip)
button_clear = Button(frame, text="Clear", command=clear_entries)

# position widgets on screen - using the function pack()
# parameter(frame has 10px padding, x and y each)
frame.pack(padx=10, pady=10)
input_label.pack(anchor="w")        # position of the label (w: west)
input_entry.pack(pady=(0, 10))

radiobutton_encript.pack(anchor="w")
radiobutton_decript.pack(anchor="w")

# position of the label (w: west)
output_label.pack(anchor="w", pady=(5, 0))
output_entry.pack(pady=(0, 10))
button_execute.pack(side="right")  # button to the right
button_clear.pack(side="left")     # button to the left


# make the window visual
window.mainloop()
