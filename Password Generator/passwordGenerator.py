import tkinter as tk
from tkinter import messagebox, font
import random
import string

# generation 
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(characters, k=length))
        password_output.config(text=password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

#gui
app = tk.Tk()
app.title("Generator")
app.geometry("480x400")
app.configure(bg="#fff0f5")  # Pastel pink

app_font = font.Font(family="Comic Sans MS", size=13)

# Colors
pastel_purple = "#e3d7ff"
pastel_blue = "#d0f4f6"
pastel_green = "#ccf5d3"
pastel_yellow = "#fff7c3"

title = tk.Label(app, text="Password Generator", font=("Comic Sans MS", 18, "bold"), bg="#fff0f5", fg="#5c5470")
title.pack(pady=25)

# len
length_label = tk.Label(app, text="Enter Password Length:", font=app_font, bg="#fff0f5")
length_label.pack(pady=10)

length_entry = tk.Entry(app, font=app_font, width=20, bd=2, relief="groove", bg=pastel_blue)
length_entry.pack(pady=5)

#generate
generate_btn = tk.Button(app, text="Generate Password", font=app_font, bg=pastel_green, width=20,
                         activebackground=pastel_purple, command=generate_password)
generate_btn.pack(pady=20)

#output:
output_label = tk.Label(app, text="Generated Password:", font=("Comic Sans MS", 14, "bold"), bg="#fff0f5", fg="#4d4b57")
output_label.pack(pady=10)

password_output = tk.Label(app, text="", font=("Courier", 14), bg="#fff0f5", fg="#2e2e2e", wraplength=400)
password_output.pack(pady=5)

footer = tk.Label(app, text="Made by Rituja", font=("Comic Sans MS", 10), bg="#fff0f5", fg="gray")
footer.pack(side=tk.BOTTOM, pady=15)

app.mainloop()
