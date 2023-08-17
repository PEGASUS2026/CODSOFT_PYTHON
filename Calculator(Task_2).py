import tkinter as tk
from math import sqrt

def on_button_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "√":
        try:
            num = float(screen.get())
            result = str(sqrt(num))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "x²":
        try:
            num = float(screen.get())
            result = str(num ** 2)
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "x³":
        try:
            num = float(screen.get())
            result = str(num ** 3)
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    else:
        screen.set(screen.get() + text)

# Create a GUI window
root = tk.Tk()
root.geometry("400x500")
root.title("Calculator")

# Create a text entry field
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4, ipadx=8, padx=10, pady=10)

# Create buttons
button_text = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+"),
    ("√", "x²", "x³", ".")
]

for i, row in enumerate(button_text):
    button_row = tk.Frame(root)
    button_row.grid(row=i + 1, column=0, columnspan=4, sticky="nsew")
    for j, text in enumerate(row):
        button = tk.Button(button_row, text=text, font=("Helvetica", 20), relief="ridge", bd=3, width=7, height=2)
        button.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")
        button.bind("<Button-1>", on_button_click)

# Configure grid
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the GUI event loop
root.mainloop()