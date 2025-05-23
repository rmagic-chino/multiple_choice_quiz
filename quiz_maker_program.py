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

    #ask user to save questions before exiting
def exit_program():
    if messagebox.askyesno("Exit", "Do you want to save questions before exiting?"):
        save_question_to_file()
    root.destroy()

#create main window
root = tk.Tk()
root.title("Question Entry Tool")
root.geometry("420x520")

#question input fields
tk.Label(root, text="Enter your question:").pack()
entry_question = tk.Entry(root, width=60)
entry_question.pack()

tk.Label(root, text="Option a:").pack()
entry_option_a = tk.Entry(root, width=60)
entry_option_a.pack()

tk.Label(root, text="Option b:").pack()
entry_option_b = tk.Entry(root, width=60)
entry_option_b.pack()

tk.Label(root, text="Option c:").pack()
entry_option_c = tk.Entry(root, width=60)
entry_option_c.pack()

tk.Label(root, text="Option d:").pack()
entry_option_d = tk.Entry(root, width=60)
entry_option_d.pack()

#correct answer selection
tk.Label(root, text="Select the correct answer:").pack()
correct_option = tk.StringVar()

radio_frame = tk.Frame(root)
radio_frame.pack()

tk.Radiobutton(radio_frame, text="a", variable=correct_option, value='a').pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="b", variable=correct_option, value='b').pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="c", variable=correct_option, value='c').pack(side=tk.LEFT)
tk.Radiobutton(radio_frame, text="d", variable=correct_option, value='d').pack(side=tk.LEFT)

#buttons
tk.Button(root, text="Add Question", width=20, command=submit_question).pack(pady=15)
tk.Button(root, text="Exit", width=20, command=exit_program).pack()

#start program
root.mainloop()
