import tkinter as tk
from tkinter import messagebox, font

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result_label.config(text="Invalid Operation")
            return

        result_label.config(text=f"Result: {result:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

#gui
app = tk.Tk()
app.title("Calculator")
app.geometry("420x450")
app.configure(bg="#fceef5")

app_font = font.Font(family="Comic Sans MS", size=13)

#colors:
pastel_pink = "#fddde6"
pastel_blue = "#d0f4f6"
pastel_yellow = "#fff5c3"
pastel_green = "#d6f5d6"
pastel_violet = "#e7d3f7"
accent = "#c9e4de"

#title
title = tk.Label(app, text="Calculator", font=("Comic Sans MS", 20, "bold"),
                 bg="#fceef5", fg="#6a5d7b")
title.pack(pady=25)

#input fields
entry1 = tk.Entry(app, font=app_font, width=22, bd=2, relief="groove", bg=pastel_blue)
entry1.pack(pady=10)

entry2 = tk.Entry(app, font=app_font, width=22, bd=2, relief="groove", bg=pastel_blue)
entry2.pack(pady=10)

#Operator
operator = tk.StringVar()
operator.set('+')

op_menu = tk.OptionMenu(app, operator, '+', '-', '*', '/')
op_menu.config(font=app_font, bg=pastel_violet, fg="black", width=10, bd=1)
op_menu.pack(pady=15)

#calculate button-
calc_btn = tk.Button(app, text="Calculate", command=calculate, font=app_font,
                     bg=pastel_green, fg="black", activebackground=accent, width=18)
calc_btn.pack(pady=10)

# result
result_label = tk.Label(app, text="Result: ", font=("Comic Sans MS", 15, "bold"),
                        bg="#fceef5", fg="#555")
result_label.pack(pady=25)

# footer
footer = tk.Label(app, text="Made by Rituja", font=("Comic Sans MS", 10),
                  bg="#fceef5", fg="gray")
footer.pack(side=tk.BOTTOM, pady=10)

app.mainloop()
