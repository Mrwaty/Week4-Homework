import random
import string
import tkinter as tk

lowercase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
digits=["1","2","3","4","5","6","7","8","9","0"]
#characters=string.ascii_uppercase() + string.ascii_lowercase() + string.digits() + string.punctuation()
characters= lowercase + uppercase + symbols + digits

def random_password():
    random_list= random.sample(digits,2) + random.sample(uppercase,2) + random.sample(symbols,2) + random.sample(characters,4)
    password= "".join(random.sample(random_list,10))
    label_.config(text= password)
    #return a

window = tk.Tk()

window.title("Random Password")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="PASSWORD", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label_ = tk.Label(key_application, text="Please push the button to choose a random password", font="arial 12")
label_.grid(padx=110, pady=20)

# button
button1 = tk.Button(window, text=" CHOOSE ", width=50, height=5, command=random_password)
button1.grid(padx=110, pady=40)

window.mainloop()

"""
General Information:
I want to use a program which can generate random password and display the result on user interface. 

Acceptance Criteria:

* Use tkinter package to solve the problem. (You can use the random student codes as template)
* Password length must be 10 characters long. 
* It must contain at least 2 upper case letter, 2 digits and 2 special symbols. 
* You must import some required modules or packages. 
* The GUI of program must contain at least a button and a label (customize the screen according to yourself) 
* The result should be display on the password label when the user click the generate button.

"""