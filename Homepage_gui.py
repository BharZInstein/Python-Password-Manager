import tkinter
import tkinter.font
import random
import pyperclip
import string
import sqlite3
from random_password_gen import passgen
url=None
usr=None
password=None
website_name=None
ms_username=None

def addField_Page():
    for widget in home.winfo_children():
        widget.destroy()
    def password_gen():
        password=passgen() 
        pas_entry.insert(0, password)
        pyperclip.copy(password)

    def addEntry_DB(website_name,user_name,url,service_password):
        conn= sqlite3.connect('pass_manager.db')
        c=conn.cursor()

        c.execute("INSERT INTO user_data_storage VALUES(:url, :user_name, :service_pwd, :website_name, :M_username)",
                {
                    'website_name': website_name,
                    'user_name': user_name,
                    'url':url,
                    'service_pwd': service_password,
                    'M_username': ms_username,
                })
        conn.commit()
        conn.close()

    def addEntry():
        global url
        global usr
        global password
        global website_name
        url=url_entry.get()
        usr=usr_entry.get()
        password=pas_entry.get()
        website_name=web_entry.get()
        addEntry_DB(website_name,usr,url,password)
        an=tkinter.Label(home,text="*Successfully Added",bg="black",fg="red")
        an.place(x=5,y=290)
        return None
    home=tkinter.Tk()
    home.title("The Bois Password Manager")
    home['bg']='black'
    home.title("The Bois Password Manager - Add A New Password")
    home.geometry("920x640")
    Headin_text=tkinter.Label(home,text="The Bois password manager",bg="black",fg="green")
    Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
    Headin_text.configure(font=Custom_Font)
    Headin_text.pack()
    #url,username,password input
    url_text=tkinter.Label(home,text="URL:",bg="black",fg="green")
    url_text.place(x=5,y=42)
    url_entry=tkinter.Entry(home,width=50,fg="black", bg="#64f586")
    url_entry.place(x=150,y=42)

    usr_text=tkinter.Label(home,text="Username:",bg="black",fg="green")
    usr_text.place(x=5,y=105)
    usr_entry=tkinter.Entry(home,width=50,fg="black", bg="#64f586")
    usr_entry.place(x=150,y=105)

    pas_text=tkinter.Label(home,text="Password:",bg="black",fg="green")
    pas_text.place(x=5,y=168)
    pas_entry=tkinter.Entry(home,width=50,fg="black", bg="#64f586")
    pas_entry.place(x=150,y=168)
    pas_gen=tkinter.Button(home,text="Password Generator",bg="black",fg="green",activebackground='#64f586', command=password_gen)
    pas_gen.place(x=460,y=165)

    web_text=tkinter.Label(home, text="Website name:",bg="black",fg="green")
    web_text.place(x=5,y=225)
    web_entry=tkinter.Entry(home,width=50,fg="black", bg="#64f586")
    web_entry.place(x=150,y=225)
    Go_Button=tkinter.Button(home,text="ADD",bg="#00ff95",fg="green",width=25,height=2,activebackground='#64f586', command=addEntry)
    Go_Button.place(x=150,y=275)

    home.mainloop()

def homePage(usr):
    global ms_username
    ms_username=usr
      
    def addPage():
        addField_Page()
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