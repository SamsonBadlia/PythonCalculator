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


    one = Button(gui, text=' 1 ', fg='white', bg='black',command=lambda: press(1), height=int(width/100), width=int(length/100))
    one.grid(row=2, column=0)

    two = Button(gui, text=' 2 ', fg='white', bg='black',command=lambda: press(2), height=int(width/100), width=int(length/100))
    two.grid(row=2, column=1)

    three = Button(gui, text=' 3 ', fg='white', bg='black',command=lambda: press(3), height=int(width/100), width=int(length/100))
    three.grid(row=2, column=2)

    four = Button(gui, text=' 4 ', fg='white', bg='black',command=lambda: press(4), height=int(width/100), width=int(length/100))
    four.grid(row=3, column=0)

    five = Button(gui, text=' 5 ', fg='white', bg='black',command=lambda: press(5), height=int(width/100), width=int(length/100))
    five.grid(row=3, column=1)

    six = Button(gui, text=' 6 ', fg='white', bg='black',command=lambda: press(6), height=int(width/100), width=int(length/100))
    six.grid(row=3, column=2)

    seven = Button(gui, text=' 7 ', fg='white', bg='black',command=lambda: press(7), height=int(width/100), width=int(length/100))
    seven.grid(row=4, column=0)

    eight = Button(gui, text=' 8 ', fg='white', bg='black',command=lambda: press(8), height=int(width/100), width=int(length/100))
    eight.grid(row=4, column=1)

    nine = Button(gui, text=' 9 ', fg='white', bg='black',command=lambda: press(9), height=int(width/100), width=int(length/100))
    nine.grid(row=4, column=2)

    zero = Button(gui, text=' 0 ', fg='white', bg='black',command=lambda: press(0), height=int(width/100), width=int(length/100))
    zero.grid(row=5, column=0)

    addition = Button(gui, text=' + ', fg='white', bg='black',command=lambda: press("+"), height=int(width/100), width=int(length/100))
    addition.grid(row=2, column=3)

    subtraction = Button(gui, text=' - ', fg='white', bg='black',command=lambda: press("-"), height=int(width/100), width=int(length/100))
    subtraction.grid(row=3, column=3)

    multiplication = Button(gui, text=' * ', fg='white', bg='black',command=lambda: press("*"), height=int(width/100), width=int(length/100))
    multiplication.grid(row=4, column=3)

    division = Button(gui, text=' / ', fg='white', bg='black',command=lambda: press("/"), height=int(width/100), width=int(length/100))
    division.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='white', bg='black',command=equalpress, height=int(width/100), width=int(length/100))
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='white', bg='black',command=clear, height=int(width/100), width=int(length/100))
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='white', bg='black',command=lambda: press('.'), height=int(width/100), width=int(length/100))
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
