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
#command questions

#command for answers

#setup window
#setup labels
#setup buttons

#run the main loop
