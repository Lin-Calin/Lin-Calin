
from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualisInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


cal = Tk()
cal.title("Sicientific Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='left').grid(columnspan=6)

btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="powder blue", command=lambda: btnClick(1)).grid(row=1, column=1)

btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="powder blue", command=lambda: btnClick(2)).grid(row=1, column=2)

btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="powder blue", command=lambda: btnClick(3)).grid(row=1, column=3)

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="powder blue", command=lambda: btnClick(4)).grid(row=2, column=1)

btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="powder blue", command=lambda: btnClick(5)).grid(row=2, column=2)

btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="powder blue", command=lambda: btnClick(6)).grid(row=2, column=3)

btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="powder blue", command=lambda: btnClick(7)).grid(row=3, column=1)

btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="powder blue", command=lambda: btnClick(8)).grid(row=3, column=2)

btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="powder blue", command=lambda: btnClick(9)).grid(row=3, column=3)

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="powder blue", command=lambda: btnClick(0)).grid(row=4, column=1)

Subtraction = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="+", bg="powder blue", command=lambda: btnClick("+")).grid(row=4, column=2)

Subtraction = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="-", bg="powder blue", command=lambda: btnClick("-")).grid(row=4, column=3)

Multiply = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                  text="*", bg="powder blue", command=lambda: btnClick("*")).grid(row=5, column=1)

btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="powder blue", command=btnEqualisInput).grid(row=5, column=2)

btnClear = Button(cal, padx=16, pady=16, bd=8, fg="red", font=('arial', 20, 'bold'),
                  text="Cl", bg="powder blue", command=btnClearDisplay).grid(row=5, column=3)

Division = Button(cal, padx=16, pady=16, bd=8, fg="blue", font=('arial', 20, 'bold'),
                  text="/", bg="powder blue", command=lambda: btnClick("/")).grid(row=6, column=2)

cal.mainloop()
