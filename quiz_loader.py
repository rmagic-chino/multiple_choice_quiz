#initialize imports
import tkinter as tk
from tkinter import filedialog, messagebox
import random

#put command for question loading
def load_questions():
    global questions
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not path:
        return
    
    with open(path, 'r') as file:
        blocks = file.read().strip().split('\n\n')
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) == 6:
            questions.append({
                'q': lines[0][9:], 'a': lines[1][3:], 'b': lines[2][3:],
                'c': lines[3][3:], 'd': lines[4][3:], 'correct': lines[5][9:]
            })
    if questions:
         next_question()
    else:
        messagebox.showinfo("info", "No questions found in the file.")
        
#command questions

#command for answers

#setup window
#setup labels
#setup buttons

#run the main loop
