import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid expression")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display input and results
entry = tk.Entry(root, width=20, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons on the grid
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=button_clear)
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=lambda t=text: button_click(t))
    
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()


