from tkinter import *


# User Interface
windows = Tk()

rel_lbl = Entry(windows, font=("Bahnschrift", 20), fg= "#000000", justify="center")
rel_lbl.grid(row=0, column=0,columnspan=5)

number_1 = Button(windows, font=("Bahnschrift", 20), text= '1', fg= "#000000",width=5, height=2)
number_1.grid(row=1, column=0)

number_2 = Button(windows, font=("Bahnschrift", 20), text= '2', fg= "#000000",width=5, height=2)
number_2.grid(row=1, column=1)

number_3 = Button(windows, font=("Bahnschrift", 20), text= '3', fg= "#000000",width=5, height=2)
number_3.grid(row=1, column=2)

number_4 = Button(windows, font=("Bahnschrift", 20), text= '4', fg= "#000000",width=5, height=2)
number_4.grid(row=2, column=0)

number_5 = Button(windows, font=("Bahnschrift", 20), text= '5', fg= "#000000",width=5, height=2)
number_5.grid(row=2, column=1)

number_6 = Button(windows, font=("Bahnschrift", 20), text= '6', fg= "#000000",width=5, height=2)
number_6.grid(row=2, column=2)

number_7 = Button(windows, font=("Bahnschrift", 20), text= '7', fg= "#000000",width=5, height=2)
number_7.grid(row=3, column=0)

number_8 = Button(windows, font=("Bahnschrift", 20), text= '8', fg= "#000000",width=5, height=2)
number_8.grid(row=3, column=1)

number_9 = Button(windows, font=("Bahnschrift", 20), text= '9', fg= "#000000",width=5, height=2)
number_9.grid(row=3, column=2)

number_0 = Button(windows, font=("Bahnschrift", 20), text= '0', fg= "#000000",width=5, height=2)
number_0.grid(row=4, column=0)

clear_btn = Button(windows, font=("Bahnschrift", 20), text= 'C', fg= "#000000",width=5, height=2)
clear_btn.grid(row=4, column=1)

equal_btn = Button(windows, font=("Bahnschrift", 20), text= '=', fg= "#000000",width=5, height=2)
equal_btn.grid(row=4, column=2)


plus_btn = Button(windows, font=("Bahnschrift", 20), text= '+', fg= "#000000",width=5, height=2)
plus_btn.grid(row=1, column=4)

minus_btn = Button(windows, font=("Bahnschrift", 20), text= '-', fg= "#000000",width=5, height=2)
minus_btn.grid(row=2, column=4)

multiply_btn = Button(windows, font=("Bahnschrift", 20), text= 'X', fg= "#000000",width=5, height=2)
multiply_btn.grid(row=3, column=4)

divide_btn = Button(windows, font=("Bahnschrift", 20), text= '/', fg= "#000000",width=5, height=2)
divide_btn.grid(row=4, column=4)

windows.title("Calculator")
windows.mainloop()