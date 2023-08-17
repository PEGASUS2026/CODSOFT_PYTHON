import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Heading
        self.heading_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), fg="blue")
        self.heading_label.pack(pady=10)

        # Username
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)

        # Password Length
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(root)
        self.length_entry.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="blue", fg="white")
        self.generate_button.pack(pady=10)

        # Generated Password
        self.generated_password_label = tk.Label(root, text="Generated Password:")
        self.generated_password_label.pack(pady=5)
        self.generated_password_value = tk.Label(root, text="", bg="lightgray")
        self.generated_password_value.pack(pady=5)

        # Accept and Reset Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        
        button_width = 15  # Adjust this value to change button size
        
        self.accept_button = tk.Button(self.button_frame, text="Accept", command=self.accept_password, width=button_width)
        self.accept_button.pack(side=tk.LEFT, padx=5)
        
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset_fields, width=button_width)
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Password length should be a positive number.")
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(length))
                self.generated_password_value.config(text=password)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def accept_password(self):
        username = self.username_entry.get()
        password = self.generated_password_value.cget("text")
        if username and password:
            with open("passwords.txt", "a") as f:
                f.write(f"Username: {username:<15} Password: {password}\n")
            self.reset_fields()
            messagebox.showinfo("Success", "Password accepted and saved.")

    def reset_fields(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_value.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
