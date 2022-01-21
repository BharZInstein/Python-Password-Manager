import tkinter
import tkinter.font
from subprocess import call
from Homepage_grps import addField_Page
ms_username=None
def homePage(usr):
    global ms_username
    ms_username=usr  
    def addPage():
        addField_Page(ms_username)
    home=tkinter.Tk()
    home.title("The Bois Password Manager")
    home.geometry("920x640")
    home['bg']='black'
    title_text=tkinter.Label(home,text="HOMEPAGE",bg="black",fg="green")
    Custom_Font1=tkinter.font.Font(home,family="Ancient Modern Tales",size=64,)
    title_text.pack(pady=100)
    title_text.configure(font=Custom_Font1)
    Headin_text=tkinter.Label(home,text="----Choose an Option----",bg="black",fg="green")
    Custom_Font2=tkinter.font.Font(family="Consolas",size=14,weight="bold")
    Headin_text.configure(font=Custom_Font2)
    Headin_text.pack()
    add=tkinter.Button(home,text="Add new Password",width=20,height=2, bg="black",fg="green", activebackground='#64f586',command=addPage)
    add.pack(pady=50)
    see=tkinter.Button(home,text="View your passwords", width=20, height=2,bg="black",fg="green", activebackground='#64f586')
    see.pack()
    home.mainloop()