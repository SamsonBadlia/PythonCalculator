from tkinter import *

exp = ""

def press(num):
    # point out the global exp variable
    global exp

    # concatenation of string
    exp = exp + str(num)

    # update the exp by using set method
    equation.set(exp)


def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set(" something is wrong bud ")
        exp = ""


def clear():
    global exp
    exp = ""
    equation.set("")


if __name__ == "__main__":

    gui = Tk()
    length = int(gui.winfo_screenwidth())
    width = int(gui.winfo_screenheight())
    gui.configure(background="blue")
    gui.title("Calculator")
    gui.geometry("%dx%d" % (length, width))

    equation = StringVar()
    exp_field = Entry(gui, textvariable=equation)
    exp_field.grid(columnspan=4, ipadx=length/4)

    number = 1
    r = None
    c = None
    while number < 11:
        button = Button(gui, text=str(number), fg='white', bg='black',command=lambda: press(number%10), height=int(width/100), width=int(length/100))
        if number < 11:
            r = 4
            if number < 7:
                r = 3
                if number < 4:
                    r = 2
        if (number - 1) % 3 == 0:
            c = 0
        if (number) % 3 == 2:
            c = 1
        if (number) % 3 == 0:
            c = 2
        if (number) == 10:
            r=5
            c=0
        number += 1
        button.grid(row=r,column = c)

    plus = Button(gui, text=' + ', fg='white', bg='black',command=lambda: press("+"), height=int(width/100), width=int(length/100))
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='white', bg='black',command=lambda: press("-"), height=int(width/100), width=int(length/100))
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='white', bg='black',command=lambda: press("*"), height=int(width/100), width=int(length/100))
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='white', bg='black',command=lambda: press("/"), height=int(width/100), width=int(length/100))
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='black',command=equalpress, height=int(width/100), width=int(length/100))
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='white', bg='black',command=clear, height=int(width/100), width=int(length/100))
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='white', bg='black',command=lambda: press('.'), height=int(width/100), width=int(length/100))
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
