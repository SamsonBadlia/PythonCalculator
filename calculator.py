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

    gui.configure(background="blue")
    gui.title("Calculator")
    gui.geometry("540x300")

    equation = StringVar()
    exp_field = Entry(gui, textvariable=equation)
    exp_field.grid(columnspan=4, ipadx=70)

    number = 1
    r = None
    c = None
    while number < 11:
        button = Button(gui, text=str(number), fg='black', bg='red',command=lambda: press(number), height=1, width=7)
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
        number += 1
        button.grid(row=r,column = c)

    # button1 = Button(gui, text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=1, width=7)
    # button1.grid(row=2, column=0)
    #
    # button2 = Button(gui, text=' 2 ', fg='black', bg='red',command=lambda: press(2), height=1, width=7)
    # button2.grid(row=2, column=1)
    #
    # button3 = Button(gui, text=' 3 ', fg='black', bg='red',command=lambda: press(3), height=1, width=7)
    # button3.grid(row=2, column=2)
    #
    # button4 = Button(gui, text=' 4 ', fg='black', bg='red',command=lambda: press(4), height=1, width=7)
    # button4.grid(row=3, column=0)
    #
    # button5 = Button(gui, text=' 5 ', fg='black', bg='red',command=lambda: press(5), height=1, width=7)
    # button5.grid(row=3, column=1)
    #
    # button6 = Button(gui, text=' 6 ', fg='black', bg='red',command=lambda: press(6), height=1, width=7)
    # button6.grid(row=3, column=2)
    #
    # button7 = Button(gui, text=' 7 ', fg='black', bg='red',command=lambda: press(7), height=1, width=7)
    # button7.grid(row=4, column=0)
    #
    # button8 = Button(gui, text=' 8 ', fg='black', bg='red',command=lambda: press(8), height=1, width=7)
    # button8.grid(row=4, column=1)
    #
    # button9 = Button(gui, text=' 9 ', fg='black', bg='red',command=lambda: press(9), height=1, width=7)
    # button9.grid(row=4, column=2)
    #
    # button0 = Button(gui, text=' 0 ', fg='black', bg='red',command=lambda: press(0), height=1, width=7)
    # button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()