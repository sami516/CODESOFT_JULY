import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = operation_var.get()

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        else:
            result = "Invalid choice."

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator")

# Create and place widgets
label_num1 = tk.Label(app, text="Enter the first number:")
label_num1.pack()
entry_num1 = tk.Entry(app)
entry_num1.pack()

label_num2 = tk.Label(app, text="Enter the second number:")
label_num2.pack()
entry_num2 = tk.Entry(app)
entry_num2.pack()

operation_var = tk.IntVar()
operation_var.set(1)  # Default choice: Addition

operation_choices = [
    ("Add", 1),
    ("Subtract", 2),
    ("Multiply", 3),
    ("Divide", 4)
]

for text, value in operation_choices:
    tk.Radiobutton(app, text=text, variable=operation_var, value=value).pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(app, text="Result:")
result_label.pack()

# Start the GUI event loop
app.mainloop()
