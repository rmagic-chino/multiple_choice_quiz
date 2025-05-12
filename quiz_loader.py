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
        messagebox.showinfo("Info", "No questions found in the file.")
        
#command questions
def next_question():
    global current
    if not questions:
        messagebox.showinfo("Done", "Quiz Finished!.")
        root_destroy()
        return
    current = random.choice(questions)
    questions.remove(current)
    question_label.config(text=current['q'])
    button_a.config(text=current['a'])
    button_b.config(text=current['b'])
    button_c.config(text=current['c'])
    button_d.config(text=current['d'])
    
#command for answers
def check(ans):
    if ans == current['correct']:
        messagebox.showinfo("Correct", "🔥 Tama pre!")
    else:
        messagebox.showinfo("Incorrect", "❌ Mali sagot!")
    next_question()
    
#setup window
root = tk.Tk()
root.title("Quiz App")
root.geometry("450x400")
root.resizable(False, False)
root.config(bg="#111")

questions = []
current = {}

#setup labels
tk.Button(
    root,
    text="Load Questions",
    command=load_questions,
    font=("Arial", 14),
),pack(pady=10)

question_label = tk.Label(
    root,
    text="Load a quiz file to start",
    font=("Arial", 14),
    bg="#111",
    fg="#white"
)
question_label.pack(pady=20)

#setup buttons
button_a = tk.Button(root, text="A", width=30, command=lambda: check('a'))
button_b = tk.Button(root, text="B", width=30, command=lambda: check('b'))
button_c = tk.Button(root, text="C", width=30, command=lambda: check('c'))
button_d = tk.Button(root, text="D", width=30, command=lambda: check('d'))

for button in [button_a, button_b, button_c, button_d]:
    button.pack(pady=5)
    