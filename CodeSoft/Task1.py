import tkinter as tk
import json

tasks = []

# Functions to handle tasks
def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def complete_task():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]["completed"] = True
        listbox.itemconfig(idx, {'bg':'lightgreen'})

# Save and load tasks from a file
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                listbox.insert(tk.END, task['task'])
    except FileNotFoundError:
        tasks = []

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

btn_complete = tk.Button(root, text="Complete Task", command=complete_task)
btn_complete.pack()

load_tasks()
root.mainloop()
