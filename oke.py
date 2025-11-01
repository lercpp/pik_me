import tkinter as tk

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)  
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)  
        entry.insert(0, "Ошибка")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("pik me")
root.configure(bg="pink")

entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

but = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'KA', 'PA', '!'  
]

row_v = 1
col_v = 0

for button in but:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, command=clear).grid(row=row_v, column=col_v)
    else:
        tk.Button(root, text=button, padx=20, pady=20,
                  command=lambda b=button: entry.insert(tk.END, b) if b != '=' else calculate()).grid(row=row_v, column=col_v)
    col_v += 1
    if col_v > 3:
        col_v = 0
        row_v += 1

root.mainloop()
