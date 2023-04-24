
# ICE 12
# File name : HSTcalculator.pyw

# Name: Hongju(Eugene) Shin
# Date: December 2, 2021
# App Name: Feedback Servey
# Description: Feedback servey that collect the answers of 3 questions

# import widgets from tkinter
from tkinter import *
# replace the Tk widgets with the ttk
from tkinter.ttk import *

from tkinter import messagebox

# constants
QUESTION_1 = "How satisfied are you with our company?"
ANSWER_Q1_1 = "Satisfied"
ANSWER_Q1_2 = "Neutral"
ANSWER_Q1_3 = "Dissatisfied"

QUESTION_2 = "How well do our products meet your need?"
ANSWER_Q2_1 = "Very well"
ANSWER_Q2_2 = "Somewhat well"
ANSWER_Q2_3 = "Not well"

QUESTION_3 = "Would you recommend our products to friends?"
ANSWER_Q3_1 = "For sure"
ANSWER_Q3_2 = "Not sure"
ANSWER_Q3_3 = "Surely.. not!"


# functions
def submit_click():
    """Executed when the submit button is clicked
    * Show an error pop-up when a question is left unanswered

    """
    if answer_question1.get() == "" or answer_question2.get() == "" or answer_question3.get() =="" :
        messagebox.showwarning("Warning!", "Please answer all questions!")

    else:
        report = f"""
        {QUESTION_1}
        {answer_question1.get()}
        {QUESTION_1}
        {answer_question2.get()}
        {QUESTION_1}
        {answer_question3.get()}
        """
        messagebox.showinfo("Report", report)

        # reset all the answers to unchecked
        answer_question1.set("")
        answer_question2.set("")
        answer_question3.set("")


# set up the window
window = Tk()     # creat a new window
window.title("Survey - Eugene")              # set the title
window.iconbitmap("Survey.ico")              # change the window icon
window.resizable(width=False, height=False)  # set the window not resizable


# 3 label frames for the questions
question1frame = LabelFrame(text=QUESTION_1)
question2frame = LabelFrame(text=QUESTION_2)
question3frame = LabelFrame(text=QUESTION_3)

# ====================================================================================================
# Question 1 radio buttons
# ====================================================================================================
answer_question1 = Variable()  # variable used in the radiobutton
q1a1_radiobutton = Radiobutton(question1frame, text=ANSWER_Q1_1, variable=answer_question1, value=ANSWER_Q1_1)
q1a2_radiobutton = Radiobutton(question1frame, text=ANSWER_Q1_2, variable=answer_question1, value=ANSWER_Q1_2)
q1a3_radiobutton = Radiobutton(question1frame, text=ANSWER_Q1_3, variable=answer_question1, value=ANSWER_Q1_3)

# ====================================================================================================
# Question 2 radio buttons
# ====================================================================================================
answer_question2 = Variable()  # variable used in the radiobutton
q2a1_radiobutton = Radiobutton(question2frame, text=ANSWER_Q2_1, variable=answer_question2, value=ANSWER_Q2_1)
q2a2_radiobutton = Radiobutton(question2frame, text=ANSWER_Q2_2, variable=answer_question2, value=ANSWER_Q2_2)
q2a3_radiobutton = Radiobutton(question2frame, text=ANSWER_Q2_3, variable=answer_question2, value=ANSWER_Q2_3)

# ====================================================================================================
# Question 3 radio buttons
# ====================================================================================================
answer_question3 = Variable()  # variable used in the radiobutton
q3a1_radiobutton = Radiobutton(question3frame, text=ANSWER_Q3_1, variable=answer_question3, value=ANSWER_Q3_1)
q3a2_radiobutton = Radiobutton(question3frame, text=ANSWER_Q3_2, variable=answer_question3, value=ANSWER_Q3_2)
q3a3_radiobutton = Radiobutton(question3frame, text=ANSWER_Q3_3, variable=answer_question3, value=ANSWER_Q3_3)

# submit button
submit_button = Button(text="Submit Answers", command=submit_click)



# ====================================================================================================
# Place the widgets using pack()
# ====================================================================================================
question1frame.pack(fill="x", padx=10, pady=5)     # x: horizontal space fill
q1a1_radiobutton.pack(anchor="w")       # align to the left
q1a2_radiobutton.pack(anchor="w")       # align to the left
q1a3_radiobutton.pack(anchor="w")       # align to the left

question2frame.pack(fill="x", padx=10, pady=5)     # x: horizontal space fill
q2a1_radiobutton.pack(anchor="w")       # align to the left
q2a2_radiobutton.pack(anchor="w")       # align to the left
q2a3_radiobutton.pack(anchor="w")       # align to the left

question3frame.pack(fill="x", padx=10, pady=5)     # x: horizontal space fill
q3a1_radiobutton.pack(anchor="w")       # align to the left
q3a2_radiobutton.pack(anchor="w")       # align to the left
q3a3_radiobutton.pack(anchor="w")       # align to the left

submit_button.pack(pady=(5,10))         # padding top = 5, bottom = 10



# make the window visual
window.mainloop()