import tkinter as tk
from tkinter import messagebox, font

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        update_listbox()
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = True
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to mark as done")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✗"
        listbox.insert(tk.END, f"[{status}] {task['task']}")

# ----- GUI Setup -----
app = tk.Tk()
app.title("📝 To-Do List")
app.geometry("600x500")  # Bigger window

# Custom font
app_font = font.Font(family="Helvetica", size=12)

# Entry field
task_entry = tk.Entry(app, width=50, font=app_font, bd=2)
task_entry.pack(pady=20)

# Buttons Frame
btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="➕ Add Task", width=15, font=app_font, bg="#a3d2ca", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="✅ Mark as Done", width=15, font=app_font, bg="#f7d794", command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

del_btn = tk.Button(btn_frame, text="❌ Delete Task", width=15, font=app_font, bg="#f8a5c2", command=delete_task)
del_btn.grid(row=0, column=2, padx=5)

# Listbox with scrollbar
listbox_frame = tk.Frame(app)
listbox_frame.pack(pady=20)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, width=70, height=15, font=app_font, yscrollcommand=scrollbar.set, bd=2)
listbox.pack()

scrollbar.config(command=listbox.yview)

# Start app loop
app.mainloop()
