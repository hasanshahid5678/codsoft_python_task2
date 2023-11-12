from tkinter import *
from tkinter.ttk import *
from ttkbootstrap.constants import *
import ttkbootstrap
from PIL import Image, ImageTk

root = ttkbootstrap.Window(themename="solar")
root.title("calculator")
im = Image.open('calculator_icon.png').resize((20,20),Image.LANCZOS)
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)


a = ""
b = ""
result = 0
operator = ""
def numf(i):
    global operator, result, b
    if not operator and not result:
        if ans_field.cget("text") == "0":
            ans_field.config(text = i)
        else:
            ans_field.config(text=ans_field.cget("text") + i)
    else:
        if ans_field.cget("text") == input_field.get()[0 : len(input_field.get()) - 1]:
            ans_field.config(text = i)
            b = ans_field.cget("text")
        else:
            ans_field.config(text=ans_field.cget("text") + i)
            b = ans_field.cget("text")


def operate(o):
    global a, b, operator
    if not operator and not a:
        a = ans_field.cget("text")
        operator = o
        input_field.delete(0, END)
        input_field.insert(0, a + o)
    elif not b:
        operator = o
        input_field.delete(len(input_field.get()) - 1, END)
        input_field.insert(END, o)
    else:
        result = calculate(a, b)
        a = result
        b = ""
        input_field.delete(0, END)
        input_field.insert(0, result + o)
        operator = o

def equatef():
    global a, b, operator, result
    if not operator:
        input_field.delete(0, END)
        input_field.insert(0, ans_field.cget("text") + "=")
    else:
        input_field.insert(END, ans_field.cget("text") + "=")
        result = calculate(a, ans_field.cget("text"))

        



def clearf():
    global a, b, operator, ans_field, result
    input_field.delete(0, END)
    ans_field.config(text="0")
    a = ""
    b = ""
    operator = ""
    result = 0
    num_button0.configure(state="normal")
    num_button1.configure(state="normal")
    num_button2.configure(state="normal")
    num_button3.configure(state="normal")
    num_button4.configure(state="normal")
    num_button5.configure(state="normal")
    num_button6.configure(state="normal")
    num_button7.configure(state="normal")
    num_button8.configure(state="normal")
    num_button9.configure(state="normal")
    for btn in op_buttons[:5]:
        btn.configure(state="normal")

def calculate(a, b):
    global operator, result, ans_field
    if operator == "+":
        result = float(a) + float(b)
    elif operator == "-":
        result = float(a) - float(b)
    elif operator == "×":
        result = float(a) * float(b)
    elif operator == "÷":
        try:
            result = float(a) / float(b)
        except ZeroDivisionError:
            result = "cannot Divide By Zero"
            num_button0.configure(state="disabled")
            num_button1.configure(state="disabled")
            num_button2.configure(state="disabled")
            num_button3.configure(state="disabled")
            num_button4.configure(state="disabled")
            num_button5.configure(state="disabled")
            num_button6.configure(state="disabled")
            num_button7.configure(state="disabled")
            num_button8.configure(state="disabled")
            num_button9.configure(state="disabled")
            for btn in op_buttons[:5]:
                btn.configure(state="disabled")
    if result != "cannot Divide By Zero":
        if result == int(result):
            result = int(result)
    ans_field.config(text = str(result))
    return str(result)



#Create a input field
input_field = Entry(root, width=30, justify = RIGHT)
input_field.grid(row = 0, column = 0, columnspan=10, pady=20)
input_field.insert(0, "0")
#Remove functionality of keyboard for calculator
input_field.bind("<Key>", lambda f: None)
#Create answer field
ans_field = ttkbootstrap.Label(root, text= str(0),bootstyle = "inverse", width= 20, anchor="center")
ans_field.grid(row = 1, column = 0, columnspan=10, pady = 20)
#Create number buttons
num_button7 = ttkbootstrap.Button(root, text="7", bootstyle = "success, outline", command = lambda: numf("7"))
num_button7.grid(row = 2, column = 0, padx = 5, pady = 5)
num_button8 = ttkbootstrap.Button(root, text="8", bootstyle = "success, outline", command = lambda: numf("8"))
num_button8.grid(row = 2, column = 1, padx = 5, pady = 5)
num_button9 = ttkbootstrap.Button(root, text="9", bootstyle = "success, outline", command = lambda: numf("9"))
num_button9.grid(row = 2, column = 2, padx = 5, pady = 5)
num_button4 = ttkbootstrap.Button(root, text="4", bootstyle = "success, outline", command = lambda: numf("4"))
num_button4.grid(row = 3, column = 0, padx = 5, pady = 5)
num_button5 = ttkbootstrap.Button(root, text="5", bootstyle = "success, outline", command = lambda: numf("5"))
num_button5.grid(row = 3, column = 1, padx = 5, pady = 5)
num_button6 = ttkbootstrap.Button(root, text="6", bootstyle = "success, outline", command = lambda: numf("6"))
num_button6.grid(row = 3, column = 2, padx = 5, pady = 5)
num_button1 = ttkbootstrap.Button(root, text="1", bootstyle = "success, outline", command = lambda: numf("1"))
num_button1.grid(row = 4, column = 0, padx = 5, pady = 5)
num_button2 = ttkbootstrap.Button(root, text="2", bootstyle = "success, outline", command = lambda: numf("2"))
num_button2.grid(row = 4, column = 1, padx = 5, pady = 5)
num_button3 = ttkbootstrap.Button(root, text="3", bootstyle = "success, outline", command = lambda: numf("3"))
num_button3.grid(row = 4, column = 2, padx = 5, pady = 5)
num_button0 = ttkbootstrap.Button(root, text="0", bootstyle = "success, outline", command = lambda: numf("0"))
num_button0.grid(row = 5, column = 1, padx = 5, pady = 5)

#Create operator buttons
operators = ["+", "-", "×", "÷", "=", "C"]
op_buttons = []
for i in range(len(operators)):
    if operators[i] == "+":
        op_buttons.append(ttkbootstrap.Button(root, text=operators[i], bootstyle = "success, outline", command = lambda: operate("+")))
        op_buttons[i].grid(row = 4, column=3, padx = 5, pady = 5)
    elif operators[i] == "-":
        op_buttons.append(ttkbootstrap.Button(root, text=operators[i], bootstyle = "success, outline", command = lambda: operate("-")))
        op_buttons[i].grid(row = 3, column=3, padx = 5, pady = 5)
    elif operators[i] == "C":
        op_buttons.append(ttkbootstrap.Button(root, text=operators[i], bootstyle = "success, outline", command = clearf))
        op_buttons[i].grid(row = 2, column=3, padx = 5, pady = 5)
    elif operators[i] == "÷":
        op_buttons.append(ttkbootstrap.Button(root, text=operators[i], bootstyle = "success, outline", command = lambda: operate("÷")))
        op_buttons[i].grid(row = 5, column=2, padx = 5, pady = 5)
    elif operators[i] == "×":
        op_buttons.append(ttkbootstrap.Button(root, text=operators[i], bootstyle = "success, outline", command = lambda: operate("×")))
        op_buttons[i].grid(row = 5, column=0, padx = 5, pady = 5)
    else:
        op_buttons.append(ttkbootstrap.Button(root, text=operators[i], bootstyle = "success, outline", command = equatef))
        op_buttons[i].grid(row = 5, column=3, padx = 5, pady = 5)


root.mainloop()