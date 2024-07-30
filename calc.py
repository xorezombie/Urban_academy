import tkinter as tk

def button_click(number):
    current = number_place.get()
    number_place.delete(0, tk.END)
    number_place.insert(tk.END, current + str(number))

def button_operation(op):
    global first_number
    global operation
    first_number = float(number_place.get())
    operation = op
    number_place.delete(0, tk.END)
def button_equal():
    second_number = float(number_place.get())
    number_place.delete(0, tk.END)
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    number_result.delete(0, tk.END)
    number_result.insert(tk.END, str(result))

def button_clear():
    number_place.delete(0, tk.END)
    number_result.delete(0, tk.END)



window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text= '+', width=2, height=2, command=lambda: button_operation('+'))
button_add.place(x = 280, y = 100)
button_sub = tk.Button(window, text= '-', width=2, height=2, command=lambda: button_operation('-'))
button_sub.place(x = 280, y = 150)
button_mul = tk.Button(window, text= '*', width=2, height=2, command=lambda: button_operation('*'))
button_mul.place(x = 280, y = 200)
button_div = tk.Button(window, text= '/', width=2, height=2, command=lambda: button_operation('/'))
button_div.place(x = 280, y = 250)
button_1 = tk.Button(window, text= '1', width=3, height=2, command=lambda: button_click(1))
button_1.place(x = 30, y = 100)
button_2 = tk.Button(window, text= '2', width=3, height=2, command=lambda: button_click(2))
button_2.place(x = 100, y = 100)
button_3 = tk.Button(window, text= '3', width=3, height=2, command=lambda: button_click(3))
button_3.place(x = 170, y = 100)
button_4 = tk.Button(window, text= '4', width=3, height=2, command=lambda: button_click(4))
button_4.place(x = 30, y = 150)
button_5 = tk.Button(window, text= '5', width=3, height=2, command=lambda: button_click(5))
button_5.place(x = 100, y = 150)
button_6 = tk.Button(window, text= '6', width=3, height=2, command=lambda: button_click(6))
button_6.place(x = 170, y = 150)
button_7 = tk.Button(window, text= '7', width=3, height=2, command=lambda: button_click(7))
button_7.place(x = 30, y = 200)
button_8 = tk.Button(window, text= '8', width=3, height=2, command=lambda: button_click(8))
button_8.place(x = 100, y = 200)
button_9 = tk.Button(window, text= '9', width=3, height=2, command=lambda: button_click(9))
button_9.place(x = 170, y = 200)
button_0 = tk.Button(window, text= '0', width=3, height=2, command=lambda: button_click(0))
button_0.place(x = 100, y = 250)
button_equal = tk.Button(window, text='=', width=3, height=2, command=button_equal)
button_equal.place(x=170, y=250)
button_clear = tk.Button(window, text='C', width=3, height=2, command=button_clear)
button_clear.place(x=30, y=250)
number_place = tk.Entry(window, width=15)
number_place.place(x = 75, y = 40)
number_result = tk.Entry(window, width=15)
number_result.place(x = 75, y = 300)
window.mainloop()