import tkinter
from Homepage_grps import add
import tkinter
win=tkinter.Tk()
win.title("The Bois Password Manager")
win.geometry("920x640")
win['bg']='black'
title_text=tkinter.Label(text="HOMEPAGE",bg="black",fg="green")
Custom_Font1=tkinter.font.Font(family="Ancient Modern Tales",size=64,)
title_text.pack(pady=100)
title_text.configure(font=Custom_Font1)
Headin_text=tkinter.Label(text="----Choose an Option----",bg="black",fg="green")
Custom_Font2=tkinter.font.Font(family="Consolas",size=14,weight="bold")
Headin_text.configure(font=Custom_Font2)
Headin_text.pack()
ADD=tkinter.Button(text="Add new Password",width=20,height=2, bg="black",fg="green", activebackground='#64f586',command=add)
ADD.pack(pady=50)
see=tkinter.Button(text="View your passwords", width=20, height=2,bg="black",fg="green", activebackground='#64f586')
see.pack()
search=tkinter.Button(text="Search Your Entry",width=20,height=2,bg="black",fg="green", activebackground='#64f586')
search.pack(pady=50)
win.mainloop()