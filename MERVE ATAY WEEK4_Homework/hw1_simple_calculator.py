from turtle import right
from tkinter import *
from math import ceil

def add_():
    if enter_1.get().isdigit() and enter_2.get().isdigit():
        
        num1= float(enter_1.get())
        num2= float(enter_2.get())
        result.configure(text=str(num1+num2))
        
def subtract_():
    if enter_1.get().isdigit() and enter_2.get().isdigit():
        
        num1= float(enter_1.get())
        num2= float(enter_2.get())
        result.configure(text=str(num1-num2))
        
def multiply_():
    if enter_1.get().isdigit() and enter_2.get().isdigit():
        
        num1= float(enter_1.get())
        num2= float(enter_2.get())
        result.configure(text=str(num1*num2))
        
def division_():
    if enter_1.get().isdigit() and enter_2.get().isdigit():
        
        num1= float(enter_1.get())
        num2= float(enter_2.get())
        result.configure(text=str(num1/num2))
        
def quit_():
    quit()
    
def clear_():
    enter_1.delete(0, "end")
    enter_2.delete(0,"end")
    result.configure(text="")
    


window=Tk()
window.title("Calculator")
window.geometry("300x300")

result= Label(window, text="RESULT")
result.place(relx=0.45 , rely=0.1)

enter_1= Entry(window, width=40, justify="right")
enter_1.place(relx=0.1, rely=0.2, relheight=0.1, relwidth=0.8)

enter_2= Entry(window, width=40, justify="right")
enter_2.place(relx=0.1, rely=0.3, relheight=0.1, relwidth=0.8)

button_addition= Button(window, text="+", command= add_)
button_addition.place(relx=0.3, rely= 0.4, relheight=0.1 , relwidth=0.4)

button_subtraction= Button(window, text="-", command= subtract_)
button_subtraction.place(relx=0.3, rely= 0.5, relheight=0.1 , relwidth=0.4)

button_multiplication= Button(window, text="x", command= multiply_)
button_multiplication.place(relx=0.3, rely= 0.6, relheight=0.1 , relwidth=0.4)

button_division= Button(window, text="/", command= division_)
button_division.place(relx=0.3, rely= 0.7, relheight=0.1 , relwidth=0.4)

button_quit= Button(window, text="QUIT", command= quit_)
button_quit.place(relx= 0.3, rely=0.9, relheight=0.1 ,relwidth=0.4 )

button_clear= Button(window, text="CLEAR", command= clear_)
button_clear.place(relx= 0.3, rely=0.8, relheight=0.1 ,relwidth=0.4 )


window.mainloop()