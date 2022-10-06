import string
from random import randint, choice
from tkinter import *

def generate_password():
    
    password_max = 30
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars)for x in range(password_max))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


#1er fenetre
window = Tk()
window.title("GenDax | générateur de mot de passe")
window.geometry("400x600")
window.config(background='#403E3E')

# creer la frame principale
frame= Frame(window, bg='#403E3E')

#creer un sous boite
right_frame = Frame(frame, bg='#403E3E')



#creer un titre
label_title = Label(right_frame, text="", font=("helvetica", 20), bg='#403E3E', fg='black')
label_title.pack()

#creer un champ/input

password_entry = Entry(right_frame, font=("helvetica", 20), bg='#403E3E', fg='white')
password_entry.pack()
#creer un BOUTON
generate_password_button = Button(right_frame, text="GENERATE", font=("Impact", 20), bg='#403E3E', fg='white', command=generate_password)
generate_password_button.pack(fill=X)


right_frame.grid(row=0, column=1, sticky=W)
#afficher la frame

frame.pack(expand=YES)

#afficher la barre de menu
menu_bar = Menu(window)
#creer 1er menu
#file_menu = Menu(menu_bar, tearoff=0)
#file_menu.add_command(label="Crée nouveau Password", command = generate_password)
#file_menu.add_command(label="Fermer le Générateur", command=window.quit)
#menu_bar.add_cascade(label="Sandax", menu=file_menu)

# ajouter menu bar
window.config(menu=menu_bar)



#afficher fenetre
window.mainloop()