import string
from random import randint, choice
from tkinter import *

def generate_password():
    
    password_max = 30
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars)for x in range(password_max))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# WINDOW
window = Tk()
window.title("GenDax | générateur de mot de passe")
window.geometry("400x600")
window.config(background='#403E3E')


frame= Frame(window, bg='#403E3E')


right_frame = Frame(frame, bg='#403E3E')




label_title = Label(right_frame, text="", font=("helvetica", 20), bg='#403E3E', fg='black')
label_title.pack()



password_entry = Entry(right_frame, font=("helvetica", 20), bg='#403E3E', fg='white')
password_entry.pack()


generate_password_button = Button(right_frame, text="GENERATE", font=("Impact", 20), bg='#403E3E', fg='white', command=generate_password)
generate_password_button.pack(fill=X)


right_frame.grid(row=0, column=1, sticky=W)


frame.pack(expand=YES)



window.mainloop()
