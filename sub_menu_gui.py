from tkinter import *
from sub_menu_grps import add
win=Tk()
win.title("The Bois Password Manager")
win.geometry("920x640")
Headin_text=Label(text="Choose a Option")
Headin_text.pack()
ADD=Button(text="Add a Entry",width=20,height=2, command=add)
ADD.pack(pady=100)
see=Button(text="View your passwords", width=20, height=2)
see.pack()
search=Button(text="Search Your Entry",width=20,height=2)
search.pack(pady=100)
win.mainloop()