from tkinter import *
import math
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
    except NameError:
        rel_entry.delete(0,END)
        rel_entry.insert(0,"Syntax ERROR")
def clear():
    rel_entry.delete(0,END)

def phtr2():
    pr2 = Toplevel(windows)
    label_1 = Label(pr2, text= "Hệ số a: ", font=("Bahnschrift", 15))
    label_1.grid(row=0, column=0)

    entry_1 = Entry(pr2, font=("Bahnschrift", 15), justify="center", width=6)
    entry_1.grid(row=0, column=1)

    label_2 = Label(pr2, text= "Hệ số b: ", font=("Bahnschrift", 15))
    label_2.grid(row=1, column=0)

    entry_2 = Entry(pr2, font=("Bahnschrift", 15), justify="center", width=6)
    entry_2.grid(row=1, column=1)

    label_3 = Label(pr2, text= "Hệ số c: ", font=("Bahnschrift", 15))
    label_3.grid(row=2, column=0)

    entry_3 = Entry(pr2, font=("Bahnschrift", 15), justify="center", width=6)
    entry_3.grid(row=2, column=1)

    submit_btn = Button(pr2, font=("Bahnschrift", 15), text= "Calculate", command= lambda: calc_x())
    submit_btn.grid(row=3, column=0, columnspan=2)

    label_msg = Label(pr2, text="", font=("Bahnschrift", 15), padx=20)
    label_msg.grid(row=0, column=3)

    label_x1 = Label(pr2, text="", font=("Bahnschrift", 15), padx=20)
    label_x1.grid(row=1, column=3)

    label_x2 = Label(pr2, text="", font=("Bahnschrift", 15), padx=20)
    label_x2.grid(row=2, column=3)


    pr2.title("Giải phương trình bậc 2")
    
    def calc_x():
        try:
            a = int(entry_1.get())
            b = int(entry_2.get())
            c = int(entry_3.get())
            delta = b**2-4*a*c
            if delta < 0:
                label_msg.config(text=f"Phương trình vô nghiệm vì Δ<0 ({delta}<0)")
                label_x1.config(text="")
                label_x2.config(text="")
            elif delta == 0:
                temp = (-b+math.sqrt(delta))/(2*a)
                label_msg.config(text=f"Phương trình có nghiệm kép vì Δ=0 ({delta}=0)")
                label_x1.config(text=f"X ={temp}")
                label_x2.config(text="")
            elif delta > 0:
                temp = (-b+math.sqrt(delta))/(2*a)
                temp_2 = (-b-math.sqrt(delta))/(2*a)
                label_msg.config(text=f"Phương trình có hai nghiệm phân biệt vì Δ>0 ({delta}>0)")
                label_x1.config(text=f"X1 ={temp}")
                label_x2.config(text=f"X2 ={temp_2}")
        except ValueError:
                label_msg.config(text="Hệ số không hợp lệ !")
                label_x1.config(text="")
                label_x2.config(text="")

        








































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
editMenu= Menu(menuBar, tearoff = 0)
modeMenu = Menu(menuBar, tearoff = 0)

menuBar.add_cascade(label="Mode", menu=modeMenu)
modeMenu.add_command(label="Tính toán thông thường")
modeMenu.add_command(label="Phương trình bậc 2", command=lambda: phtr2())
modeMenu.add_command(label="Giải hệ phương trình")

windows.config(menu=menuBar)
windows.title("Calculator")
windows.mainloop()