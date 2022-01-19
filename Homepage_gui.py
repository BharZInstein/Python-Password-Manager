import tkinter
import tkinter.font
from subprocess import call
from usr import usrCall
def addEntry():
    call(["python", "Homepage_grps.py"])
win=tkinter.Tk()
usr1=usrCall()
print(usr1)
win.title("The Bois Password Manager")
win.geometry("920x640")
win['bg']='black'
icon= tkinter.PhotoImage(file="images\icon_2.png")
win.iconphoto(False, icon)
title_text=tkinter.Label(text="HOMEPAGE",bg="black",fg="green")
Custom_Font1=tkinter.font.Font(family="Ancient Modern Tales",size=64,)
title_text.pack(pady=100)
title_text.configure(font=Custom_Font1)
Headin_text=tkinter.Label(text="----Choose an Option----",bg="black",fg="green")
Custom_Font2=tkinter.font.Font(family="Consolas",size=14,weight="bold")
Headin_text.configure(font=Custom_Font2)
Headin_text.pack()
add=tkinter.Button(text="Add new Password",width=20,height=2, bg="black",fg="green", activebackground='#64f586',command=addEntry)
add.pack(pady=50)
see=tkinter.Button(text="View your passwords", width=20, height=2,bg="black",fg="green", activebackground='#64f586')
see.pack()
win.mainloop()