import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=5, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=1, padx=5, pady=5)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.show_tasks)
        self.refresh_button.grid(row=2, column=2, padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.show_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_index] = updated_task
                self.task_entry.delete(0, tk.END)
                self.show_tasks()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.show_tasks()

    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
