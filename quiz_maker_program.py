#import for GUI
import tkinter as tk
from tkinter import messagebox, filedialog
import os

#initailize
question_bank = []

#set functions for saved questions
def submit_question():
    question = entry_question.get()
    option_a = entry_option_a.get()
    option_b = entry_option_b.get()
    option_c = entry_option_c.get()
    option_d = entry_option_d.get()
    correct_answer = correct_option.get()

    #set rules and conditions
    if not question or not option_a or not option_b or not option_c or not option_d or correct_answer not in ['a', 'b', 'c', 'd']:
        messagebox.showerror("Input Error", "Please fill all fields correctly.")
        return
#set function for saving into a file


#set a function for exit

#create GUI window
    #create labels and input fields
    #create buttons

#run program

#End
