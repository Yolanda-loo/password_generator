import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        # Password length
        self.length_label = tk.Label(root, text="Password Length: 8")
        self.length_label.pack(pady=5)
        self.length_scale = tk.Scale(root, from_=4, to=32, orient=tk.HORIZONTAL, length=200, command=self.update_length)
        self.length_scale.set(8)
        self.length_scale.pack(pady=5)

        # Character type checkboxes
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.number_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.lower_var).pack(pady=5)
        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.upper_var).pack(pady=5)
        tk.Checkbutton(root, text="Include Numbers", variable=self.number_var).pack(pady=5)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var).pack(pady=5)

        # Password display
        self.password_entry = tk.Entry(root, width=40, state='readonly')
        self.password_entry.pack(pady=10)

        # Generate button
        tk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=10)

    def update_length(self, value):
        self.length_label.config(text=f"Password Length: {value}")

    def generate_password(self):
        length = self.length_scale.get()
        use_lower = self.lower_var.get()
        use_upper = self.upper_var.get()
        use_numbers = self.number_var.get()
        use_special = self.special_var.get()

        # Check if at least one character type is selected
        if not (use_lower or use_upper or use_numbers or use_special):
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        chars = ""
        if use_lower:
            chars += string.ascii_lowercase
        if use_upper:
            chars += string.ascii_uppercase
        if use_numbers:
            chars += string.digits
        if use_special:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.config(state='normal')
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
    