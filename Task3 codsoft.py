import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_callback():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Invalid length. Please enter a positive number.")
        else:
            password = generate_password(length)
            result_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")


app = tk.Tk()
app.title("Password Generator")


label_length = tk.Label(app, text="Enter the desired length of the password:")
label_length.pack()

entry_length = tk.Entry(app)
entry_length.pack()

generate_button = tk.Button(app, text="Generate Password", command=generate_password_callback)
generate_button.pack()

result_label = tk.Label(app, text="Generated Password:")
result_label.pack()


app.mainloop()
