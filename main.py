from tkinter import *
# Build

def btn_check(btn):
    rel_entry.insert(len(rel_entry.get())+1, btn)





def calc():
    try:
        illegal_char = ["x"]
        unillegal_char = ["*"]
        quest = rel_entry.get() 
        count = 0
        for i in quest:
            if i in illegal_char:
                index = illegal_char.index(i)
                quest = quest.replace(illegal_char[index], unillegal_char[index])
            count += 1
        rel_entry.delete(0,END)
        rel_entry.insert(0, eval(quest))
    except SyntaxError:
        rel_entry.delete(0,END)
        rel_entry.insert(0,"Syntax ERROR")
    except ZeroDivisionError:
        rel_entry.delete(0,END)
        rel_entry.insert(0,"Cannot divide 0")

def clear():
    rel_entry.delete(0,END)








































# User Interface
windows = Tk()

rel_entry = Entry(windows, font=("Bahnschrift", 20), fg= "#000000", justify="center")
rel_entry.grid(row=0, column=0,columnspan=5)

number_1 = Button(windows, font=("Bahnschrift", 20), text= '1', fg= "#000000",width=5, height=2, command=lambda: btn_check(1))

number_1.grid(row=1, column=0)

number_2 = Button(windows, font=("Bahnschrift", 20), text= '2', fg= "#000000",width=5, height=2, command=lambda:btn_check(2))
number_2.grid(row=1, column=1)

number_3 = Button(windows, font=("Bahnschrift", 20), text= '3', fg= "#000000",width=5, height=2, command=lambda:btn_check(3))
number_3.grid(row=1, column=2)

number_4 = Button(windows, font=("Bahnschrift", 20), text= '4', fg= "#000000",width=5, height=2, command=lambda:btn_check(4))
number_4.grid(row=2, column=0)

number_5 = Button(windows, font=("Bahnschrift", 20), text= '5', fg= "#000000",width=5, height=2, command=lambda:btn_check(5))
number_5.grid(row=2, column=1)

number_6 = Button(windows, font=("Bahnschrift", 20), text= '6', fg= "#000000",width=5, height=2, command=lambda:btn_check(6))
number_6.grid(row=2, column=2)

number_7 = Button(windows, font=("Bahnschrift", 20), text= '7', fg= "#000000",width=5, height=2, command=lambda:btn_check(7))
number_7.grid(row=3, column=0)

number_8 = Button(windows, font=("Bahnschrift", 20), text= '8', fg= "#000000",width=5, height=2, command=lambda:btn_check(8))
number_8.grid(row=3, column=1)

number_9 = Button(windows, font=("Bahnschrift", 20), text= '9', fg= "#000000",width=5, height=2, command=lambda:btn_check(9))
number_9.grid(row=3, column=2)

number_0 = Button(windows, font=("Bahnschrift", 20), text= '0', fg= "#000000",width=5, height=2, command=lambda:btn_check(0))
number_0.grid(row=4, column=0)

clear_btn = Button(windows, font=("Bahnschrift", 20), text= 'C', fg= "#000000",width=5, height=2, command=lambda: clear())
clear_btn.grid(row=4, column=1)

equal_btn = Button(windows, font=("Bahnschrift", 20), text= '=', fg= "#000000",width=5, height=2, command=lambda:calc())
equal_btn.grid(row=4, column=2)

plus_btn = Button(windows, font=("Bahnschrift", 20), text= '+', fg= "#000000",width=5, height=2, command=lambda:btn_check("+"))
plus_btn.grid(row=1, column=4)

minus_btn = Button(windows, font=("Bahnschrift", 20), text= '-', fg= "#000000",width=5, height=2, command=lambda:btn_check("-"))
minus_btn.grid(row=2, column=4)

multiply_btn = Button(windows, font=("Bahnschrift", 20), text= 'X', fg= "#000000",width=5, height=2, command=lambda:btn_check("x"))
multiply_btn.grid(row=3, column=4)

divide_btn = Button(windows, font=("Bahnschrift", 20), text= '/', fg= "#000000",width=5, height=2, command=lambda:btn_check("/"))
divide_btn.grid(row=4, column=4)

open_bracket_btn = Button(windows, font=("Bahnschrift", 20), text= '(', fg= "#000000",width=10, height=2, command=lambda:btn_check("("))
open_bracket_btn.grid(row=5, column=0,columnspan=2)

close_bracket_btn = Button(windows, font=("Bahnschrift", 20), text= ')', fg= "#000000",width=10, height=2, command=lambda:btn_check(")"))
close_bracket_btn.grid(row=5, column=2,columnspan=4)


menuBar = Menu(windows)
fileMenu = Menu(menuBar, tearoff = 0)

menuBar.add_cascade(label="Mode", menu=fileMenu)

windows.config(menu=menuBar)
windows.title("Calculator")
windows.mainloop()