import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_display.delete(1.0, "end")
    text_display.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        text_display.delete(1.0, "end")
        text_display.insert(1.0, result)
        #calculation = result
    except Exception:
        clear_calculation()
        text_display.insert(1.0, "Error")
        #text_display.delete(1.0, "end")
        #text_display.insert(1.0, "Error")
        #calculation = ""

def clear_calculation():
    global calculation
    calculation = ""
    text_display.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator")
root.geometry("325x265")

text_display=tk.Text(root, height=2, width=16, font=("Arial", 24))
text_display.grid(row=0, column=0, columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, height=2)
btn_1.grid(row=1, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, height=2)
btn_2.grid(row=1, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, height=2)
btn_3.grid(row=1, column=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, height=2)
btn_4.grid(row=2, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, height=2)
btn_5.grid(row=2, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, height=2)
btn_6.grid(row=2, column=2)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, height=2)
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, height=2)
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, height=2)
btn_9.grid(row=3, column=2)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, height=2)
btn_0.grid(row=4, column=1)

btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, height=2)
btn_add.grid(row=1, column=3)
btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, height=2)
btn_subtract.grid(row=2, column=3)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, height=2)
btn_multiply.grid(row=3, column=3)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, height=2)
btn_divide.grid(row=4, column=3)
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=5, height=2)
btn_equal.grid(row=4, column=2)
btn_clear = tk.Button(root, text="C", command=clear_calculation, width=5, height=2)
btn_clear.grid(row=4, column=0)

root.mainloop()