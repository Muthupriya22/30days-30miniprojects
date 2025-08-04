from tkinter import *

def click_button(value):
    entry_field.insert(END, value)

def clear_entry():
    entry_field.delete(0, END)

def calculate_result():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, END)
        entry_field.insert(END, str(result))
    except:
        entry_field.delete(0, END)
        entry_field.insert(END, "Error")

root = Tk()
root.title("Real Calculator")
root.geometry("300x400")

# Entry field
entry_field = Entry(root, font=("Arial", 20), borderwidth=3, relief=RIDGE, justify="right")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipadx=10, ipady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for btn in buttons:
    if len(btn) == 4:  # = button spans full row
        Button(root, text=btn[0], font=("Arial", 18), width=28, height=2,
               bg="lightblue", command=calculate_result).grid(row=btn[1], column=btn[2], columnspan=btn[3], padx=5, pady=5)
    else:
        action = clear_entry if btn[0] == 'C' else lambda val=btn[0]: click_button(val)
        Button(root, text=btn[0], font=("Arial", 18), width=5, height=2,
               bg="lightgrey" if btn[0] != '=' else "lightblue", command=action).grid(row=btn[1], column=btn[2], padx=5, pady=5)

root.mainloop()
