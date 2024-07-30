import tkinter as tk

# Функция для обработки нажатия кнопок чисел
def button_click(number):
    current = entry_input.get()
    entry_input.delete(0, tk.END)
    entry_input.insert(tk.END, current + str(number))

# Функция для обработки нажатия кнопок операций
def button_operation(op):
    global first_number
    global operation
    first_number = float(entry_input.get())
    operation = op
    entry_input.delete(0, tk.END)

# Функция для обработки нажатия кнопки "="
def button_equal():
    second_number = float(entry_input.get())
    entry_input.delete(0, tk.END)
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    entry_result.delete(0, tk.END)
    entry_result.insert(tk.END, str(result))

# Функция для очистки поля ввода
def button_clear():
    entry_input.delete(0, tk.END)
    entry_result.delete(0, tk.END)

# Настройка окна
window = tk.Tk()
window.title("Калькулятор")

# Поля ввода и вывода
entry_input = tk.Entry(window, width=20, borderwidth=5)
entry_input.grid(row=0, column=0, columnspan=4)

entry_result = tk.Entry(window, width=20, borderwidth=5)
entry_result.grid(row=1, column=0, columnspan=4)

# Кнопки чисел
buttons = []
for i in range(9):
    buttons.append(tk.Button(window, text=str(i+1), width=5, height=2, command=lambda i=i: button_click(i+1)))

# Расположение кнопок чисел в сетке
button_zero = tk.Button(window, text='0', width=5, height=2, command=lambda: button_click(0))
button_zero.grid(row=4, column=0)

for i in range(3):
    for j in range(3):
        buttons[i*3 + j].grid(row=3-i, column=j)

# Кнопки операций
button_add = tk.Button(window, text='+', width=5, height=2, command=lambda: button_operation('+'))
button_sub = tk.Button(window, text='-', width=5, height=2, command=lambda: button_operation('-'))
button_mul = tk.Button(window, text='*', width=5, height=2, command=lambda: button_operation('*'))
button_div = tk.Button(window, text='/', width=5, height=2, command=lambda: button_operation('/'))

button_add.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_mul.grid(row=4, column=1)
button_div.grid(row=4, column=2)

# Кнопка "=" и "C" (очистить)
button_equal = tk.Button(window, text='=', width=5, height=2, command=button_equal)
button_clear = tk.Button(window, text='C', width=5, height=2, command=button_clear)

button_equal.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
# Запуск главного цикла программы
window.mainloop()