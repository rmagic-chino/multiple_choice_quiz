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
    
#store questions in list
    question_data = {
        'question': question,
        'a': option_a,
        'b': option_b,
        'c': option_c,
        'd': option_d,
        'correct': correct_answer
    }
    question_bank.append(question_data)    

#clear input fields
    entry_question.delete(0, tk.END)
    entry_option_a.delete(0, tk.END)
    entry_option_b.delete(0, tk.END)
    entry_option_c.delete(0, tk.END)
    entry_option_d.delete(0, tk.END)
    correct_option.set(None)

    messagebox.showinfo("Success", "Question added successfully!")

def save_question_to_file():
    if not question_bank:
        messagebox.showwarning("Warning", "No questions to save.")
        return

#open save dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Save Questions As"
    )
    
    #write questions to chosen file
    if file_path:
        try:
            with open(file_path, 'w') as file:
                for q in question_bank:
                    file.write(f"Question: {q['question']}\n")
                    file.write(f"A: {q['a']}\n")
                    file.write(f"B: {q['b']}\n")
                    file.write(f"C: {q['c']}\n")
                    file.write(f"D: {q['d']}\n")
                    file.write(f"Correct: {q['correct']}\n")

            messagebox.showinfo("Saved", f"Questions saved to:\n{file_path}")
        except Exception as error:
            messagebox.showerror("Error", f"Failed to save questions:\n{error}")

    #create buttons

#run program

#End
