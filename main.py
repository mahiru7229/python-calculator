from tkinter import Menu
from tkinter.ttk import *
import customtkinter
import tkinter as tk
import math
import json
import os



BTN_WIDTH = 70
BTN_HEIGHT = 70
BTN_FONT_SIZE = 35
ENTRY_FONT_SIZE = 25
ENTRY_WIDTH= 70
ENTRY_HEIGHT = 70
HOVER_COLOR = "#8c8c8c"

customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("light_gray")



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
        rel_entry.delete(0, tk.END)
        rel_entry.insert(0,eval(quest))
    except SyntaxError:
        rel_entry.delete(0, tk.END)
        rel_entry.insert(0,"Syntax ERROR")
        rel_entry.configure(state="disabled")
    except ZeroDivisionError:
        rel_entry.delete(0, tk.END)
        rel_entry.insert(0,"Math ERROR")
        rel_entry.configure(state="disabled")
    except ValueError:
        rel_entry.delete(0, tk.END)
        rel_entry.insert(0,"Math ERROR")
        rel_entry.configure(state="disabled")
    except:
        rel_entry.delete(0, tk.END)
        rel_entry.insert(0,"Syntax ERROR")
        rel_entry.configure(state="disabled")

def clear():
    rel_entry.configure(state="normal")
    rel_entry.delete(0, tk.END)


def del_calc():
    rel_entry.delete(len(rel_entry.get())-1)


def phtr1():
    phtr1_win = customtkinter.CTkToplevel()


    hs_a_lbl = customtkinter.CTkLabel(phtr1_win, text="Hệ số a: ", font=("Bahnschrift", 18))
    hs_a_lbl.grid(row=0, column=0, padx=5, pady=5)

    hs_b_lbl = customtkinter.CTkLabel(phtr1_win, text="Hệ số b: ", font=("Bahnschrift", 18))
    hs_b_lbl.grid(row=1, column=0, padx=5, pady=5)

    hs_a_entry = customtkinter.CTkEntry(phtr1_win, placeholder_text="a=?", font=("Bahnschrift", 18))
    hs_a_entry.grid(row=0,column=1,padx=5, pady=5)

    hs_b_entry = customtkinter.CTkEntry(phtr1_win, placeholder_text="b=?", font=("Bahnschrift", 18))
    hs_b_entry.grid(row=1,column=1,padx=5, pady=5)

    submit_btn = customtkinter.CTkButton(phtr1_win, text="Calculate", font=("Bahnschrift", 18), hover_color=HOVER_COLOR, command=lambda:calc_phtr1())
    submit_btn.grid(row=2, column=0, padx=5, pady=5)

    ans_lbl = customtkinter.CTkLabel(phtr1_win, text="", font=("Bahnschrift", 18))
    ans_lbl.grid(row=0, column=3, padx=5, pady=5)

    phtr1_show = customtkinter.CTkLabel(phtr1_win, text="", font=("Bahnschrift", 18))
    phtr1_show.grid(row=1, column=3, padx=5, pady=5)
    def calc_phtr1():
        try:
            a = int(hs_a_entry.get())
            b = int(hs_b_entry.get())
            temp_ans = -b/a
            ans_lbl.configure(text=f"X = {temp_ans}")
            phtr1_show.configure(text=f"Phương trình: {a}x + {b} = 0")
        except ValueError:
            ans_lbl.configure(text="Hệ số không hợp lệ")
            phtr1_show.configure(text="")
        except:
            ans_lbl.configure(text="Có gì đó không đúng, vui lòng thử lại sau")
            phtr1_show.configure(text="")
    phtr1_win.title("Giải phương trình bậc nhất")
    phtr1_win.grab_set()




def phtr2():
    
    phtr2_win = customtkinter.CTkToplevel()



    hs_a_lbl = customtkinter.CTkLabel(phtr2_win, text="Hệ số a: ", font=("Bahnschrift", 18))
    hs_a_lbl.grid(row=0, column=0, padx=5, pady=5)

    hs_b_lbl = customtkinter.CTkLabel(phtr2_win, text="Hệ số b: ", font=("Bahnschrift", 18))
    hs_b_lbl.grid(row=1, column=0, padx=5, pady=5)

    hs_c_lbl = customtkinter.CTkLabel(phtr2_win, text="Hệ số c: ", font=("Bahnschrift", 18))
    hs_c_lbl.grid(row=2, column=0, padx=5, pady=5)

    hs_a_entry = customtkinter.CTkEntry(phtr2_win, placeholder_text="a=?", font=("Bahnschrift", 18))
    hs_a_entry.grid(row=0,column=1,padx=5, pady=5)

    hs_b_entry = customtkinter.CTkEntry(phtr2_win, placeholder_text="b=?", font=("Bahnschrift", 18))
    hs_b_entry.grid(row=1,column=1,padx=5, pady=5)

    hs_c_entry = customtkinter.CTkEntry(phtr2_win, placeholder_text="c=?", font=("Bahnschrift", 18))
    hs_c_entry.grid(row=2,column=1,padx=5, pady=5)

    submit_btn = customtkinter.CTkButton(phtr2_win, text="Calculate", font=("Bahnschrift", 18), hover_color=HOVER_COLOR, command=lambda:calc_phtr2())
    submit_btn.grid(row=3, column=0, padx=5, pady=5)

    temp_desc = customtkinter.CTkLabel(phtr2_win, text="", font=("Bahnschrift", 18))
    temp_desc.grid(row=0, column=3, padx=5, pady=5)

    ans_x1_lbl = customtkinter.CTkLabel(phtr2_win, text="", font=("Bahnschrift", 18))
    ans_x1_lbl.grid(row=1, column=3, padx=5, pady=5)

    ans_x2_lbl = customtkinter.CTkLabel(phtr2_win, text="", font=("Bahnschrift", 18))
    ans_x2_lbl.grid(row=2, column=3, padx=5, pady=5)

    phtr2_show = customtkinter.CTkLabel(phtr2_win, text="", font=("Bahnschrift", 18))
    phtr2_show.grid(row=3, column=3, padx=5, pady=5)

    # def optionmenu_callback(choice):
    #     if os.path.exists(os.path.join("assets","user_setting")):
    #         with open(os.path.join("assets","user_setting","setting.json"), "w") as temp:
    #             data = json.loads(temp)
    #             data["settings"]["phtr1"]["mode"] = "0" #0 = Số thập phân (Default)
    #             data["settings"]["phtr2"]["mode"] = "0" #0 = Số thập phân (Default)
    #             json.dumps(data, indent=4)
    
    
    # dec_frac_chan = customtkinter.CTkOptionMenu(phtr2_win,values=["Số thập phân", "Phân số"], dropdown_hover_color=HOVER_COLOR, button_hover_color=HOVER_COLOR, font=("Bahnschrift", 18), command=optionmenu_callback)
    # dec_frac_chan.set("Số thập phân")
    # dec_frac_chan.grid(row=3,column=1)










    def calc_phtr2():
        try:
            a = int(hs_a_entry.get())
            b = int(hs_b_entry.get())
            c = int(hs_c_entry.get())
            delta = b**2-4*a*c
            if delta < 0:
                temp_desc.configure(text=f"Phương trình vô nghiệm vì Δ < 0 ({delta} < 0)")
                ans_x1_lbl.configure(text="")
                ans_x2_lbl.configure(text="")
            elif delta == 0:
                temp_desc.configure(text=f"Phương trình có nghiệm kép vì Δ = 0 ({delta} = 0)")
                ans_x1 = -b/(2*a)
                ans_x1_lbl.configure(text=f"X1 = X2 = {ans_x1}")
                ans_x2_lbl.configure(text="")
            elif delta >0:
                temp_desc.configure(text=f"Phương trình có hai nghiệm phân biệt vì Δ > 0 ({delta} > 0)")
                ans_x1 = (-b+math.sqrt(delta))/(2*a)
                ans_x2 = (-b-math.sqrt(delta))/(2*a)
                ans_x1_lbl.configure(text=f"X1 ={ans_x1}")
                ans_x2_lbl.configure(text=f"X2 ={ans_x2}")
            phtr2_show.configure(text=f"Phương trình: {a}x^2 + {b}x + {c} = 0")
        except ValueError:
            temp_desc.configure(text="Hệ số không hợp lệ")
            ans_x1_lbl.configure(text="")
            ans_x2_lbl.configure(text="")
            phtr2_show.configure(text="")
        except:
            temp_desc.configure(text="Có gì đó không đúng, xin vui lòng thử lại sau")
            ans_x1_lbl.configure(text="")
            ans_x2_lbl.configure(text="")
            phtr2_show.configure(text="")
    phtr2_win.title("Giải phương trình bậc hai")
    phtr2_win.grab_set()

















































windows = customtkinter.CTk()
option_frame = customtkinter.CTkFrame(master=windows)
option_frame.pack(side="left", fill="y")
# option_frame.grid(row=0, column=0, padx=15, pady=15)
# option_frame.grid_propagate(True)

calc_frame = customtkinter.CTkFrame(master=windows)
calc_frame.pack(side="right", fill="both", expand=True)
# calc_frame.grid(row=0, column=1)

button_frame = customtkinter.CTkFrame(master=calc_frame)
button_frame.grid(row=1, column=1)

phtr1_btn = customtkinter.CTkButton(master=option_frame, text="Giải phương trình bậc nhất", font=("Bahnschrift", 18), hover_color=HOVER_COLOR, command = lambda: phtr1())
phtr1_btn.grid(row=0, column=0, padx=5, pady=5)

phtr2_btn = customtkinter.CTkButton(master=option_frame, text="Giải phương trình bậc hai", font=("Bahnschrift", 18), hover_color=HOVER_COLOR,command = lambda: phtr2())
phtr2_btn.grid(row=1, column=0, padx=5, pady=5)


rel_entry = customtkinter.CTkEntry(master=calc_frame, placeholder_text="Type", font=("Bahnschrift", ENTRY_FONT_SIZE), width=ENTRY_WIDTH*4, justify="center", border_color="#474747")
rel_entry.grid(row=0, column = 1, columnspan=2)

number_1 = customtkinter.CTkButton(master=button_frame, text="1", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(1))
number_1.grid(row=1, column=0)

number_2 = customtkinter.CTkButton(master=button_frame, text="2", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(2))
number_2.grid(row=1, column=1)

number_3 = customtkinter.CTkButton(master=button_frame, text="3", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(3))
number_3.grid(row=1, column=2)

number_4 = customtkinter.CTkButton(master=button_frame, text="4", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(4))
number_4.grid(row=2, column=0)

number_5 = customtkinter.CTkButton(master=button_frame, text="5", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(5))
number_5.grid(row=2, column=1)

number_6 = customtkinter.CTkButton(master=button_frame, text="6", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(6))
number_6.grid(row=2, column=2)

number_7 = customtkinter.CTkButton(master=button_frame, text="7", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(7))
number_7.grid(row=3, column=0)

number_8 = customtkinter.CTkButton(master=button_frame, text="8", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(8))
number_8.grid(row=3, column=1)

number_9 = customtkinter.CTkButton(master=button_frame, text="9", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(9))
number_9.grid(row=3, column=2)

number_0 = customtkinter.CTkButton(master=button_frame, text="0", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(9))
number_0.grid(row=4, column=0)

clear_btn = customtkinter.CTkButton(master=button_frame, text="C", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, fg_color="#c79d04", command=lambda: clear())
clear_btn.grid(row=4, column=1)

equal_btn = customtkinter.CTkButton(master=button_frame, text="=", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, fg_color="#c79d04", command=lambda: calc())
equal_btn.grid(row=4, column=2)



plus_btn = customtkinter.CTkButton(master=button_frame, text="+", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check("+"))
plus_btn.grid(row=1, column=3)

minus_btn = customtkinter.CTkButton(master=button_frame, text="-", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check("-"))
minus_btn.grid(row=2, column=3)

multiply_btn = customtkinter.CTkButton(master=button_frame, text="X", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check("x"))
multiply_btn.grid(row=3, column=3)

divide_btn = customtkinter.CTkButton(master=button_frame, text="/", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check("/"))
divide_btn.grid(row=4, column=3)

open_bracket_btn = customtkinter.CTkButton(master=button_frame, text="(", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check("("))
open_bracket_btn.grid(row=5, column=0)

close_bracket_btn = customtkinter.CTkButton(master=button_frame, text=")", font=("Bahnschrift", BTN_FONT_SIZE), height=BTN_HEIGHT, width=BTN_WIDTH, hover_color=HOVER_COLOR, command=lambda: btn_check(")"))
close_bracket_btn.grid(row=5, column=1)

deleted_last = customtkinter.CTkButton(master=button_frame, text="Del", font=("Bahnschrift", BTN_FONT_SIZE),height=BTN_HEIGHT, hover_color=HOVER_COLOR, width=BTN_WIDTH*2, command=lambda: del_calc())
deleted_last.grid(row=5, column=2, columnspan=3)






windows.resizable(width=False, height=False)
windows.title("Calculator")
windows.mainloop()