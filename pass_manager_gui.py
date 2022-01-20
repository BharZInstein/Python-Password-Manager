#GUI FOR CSC PROJECT by Bharghav
#If your datbase file is empty run the databse_creation.py file
import tkinter
import tkinter.font
import sqlite3
import random
import pyperclip
import string
from random_password_gen import passgen
from hashing import make_pw_hash, check_pw_hash
from subprocess import call
from hashing import make_pw_hash, check_pw_hash
from Homepage_gui import homePage
M_password=None
url=None
usr=None
password=None
website_name=None
m_username=None
home=tkinter.Tk()
home.title("The Bois Password Manager")
home.geometry("920x640")
icon= tkinter.PhotoImage(file="images\icon_2.png")
home.iconphoto(False, icon)

#login GUI
def loginPage():
    def signUp(username,password):
        conn = sqlite3.connect('pass_manager.db')
        c = conn.cursor()
        
    
        c.execute("INSERT INTO user_data VALUES(:M_username, :master_pwd)",
                {
                    'M_username': username,
                    'master_pwd': password,
                })

        conn.commit() 
        conn.close()

    def signUp_Command():
        def signUp():
            global M_username
            global M_password
            M_username=user_name_entry.get()
            M_password=pass_word_entry.get()
            M_password=make_pw_hash(M_password)
            signUp(M_username,M_password)
            en=tkinter.Label(root,text="*Account Created Successfully",fg="red",bg="black")
            en.pack()
            return None
        root=tkinter.Tk()
        root.title("The Bois Password Manager - SignUp")
        root['bg']='black'
        Headin_text=tkinter.Label(root,text="SignUp",
        fg="green",bg="black")
        Font23=Custom_Font1=tkinter.font.Font(family="Ancient Modern Tales",size=25)
        Headin_text.configure(font=Font23)
        Headin_text.pack()
        Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
        Headin_text.configure(font=Custom_Font)
        user_name=tkinter.Label(root,text="Username:",fg="green",bg="black")
        Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
        user_name.configure(font=Custom_Font1)
        user_name.pack()
        user_name_entry = tkinter.Entry(root,fg="black", bg="#64f586", width=50)
        user_name_entry.pack()

        pass_word=tkinter.Label(root,text="Master Password:",fg="green",bg="black")
        pass_word.pack()
        pass_word.configure(font=Custom_Font1)
        pass_word_entry=tkinter.Entry(root,show="*",fg="black", bg="#64f586", width=50)
        pass_word_entry.pack()
        signUp_button= tkinter.Button(root,text="SignUp",width=10,height=2,bg="#61ff96",fg="black",command = signUp)
        signUp_button.pack(pady=5)
        root.mainloop()
    def Login():
        global username
        global password
        global m_username
        username=entry1.get()
        password=entry2.get()
        password=make_pw_hash(password)
        conn = sqlite3.connect('pass_manager.db')
        c = conn.cursor()
        c.execute("SELECT M_username from user_data WHERE M_username=? AND master_pwd=?", (username,password,))
        rows=c.fetchall()
        if rows==[]:
            wrg=tkinter.Label(home,text="*Wrong Username/Password",fg="red",bg="black")
            wrg.place(x=500,y=120)
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
        else:
            username=rows[0][0]
            m_username=username
            homePage()
        conn.close()
    home['bg']='black'
    Headin_text=tkinter.Label(text="The Bois password manager Login Portal",
    fg="green",bg="black")
    Headin_text.pack()
    Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
    Headin_text.configure(font=Custom_Font)
    text1=tkinter.Label(home,text="Username:",fg="green",bg="black")
    Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
    text1.configure(font=Custom_Font1)
    text1.pack(pady=20,side=tkinter.TOP,anchor="w")
    entry1 = tkinter.Entry(fg="black", bg="#64f586", width=50)
    entry1.place(x=100,y=50)

    text2=tkinter.Label(home,text="Master Password:",fg="green",bg="black")
    text2.pack(pady=20,side=tkinter.TOP,anchor="w")
    text2.configure(font=Custom_Font1)
    entry2=tkinter.Entry(show="*",fg="black", bg="#64f586", width=50)
    entry2.place(x=180,y=120)
    username=None
    password=None
    #Login button
    Login_button= tkinter.Button(
        text="Login",
        width=10,
        height=2,
        bg="#61ff96",
        fg="black",
        command=Login
    )
    signUp_button= tkinter.Button(
        text="SignUp",
        width=10,
        height=2,
        bg="#61ff96",
        fg="black",
        command = signUp_Command
    )
    signUp_button.pack()
    Login_button.pack()
    direc="images\matrix.gif"
    frameCnt = 20
    frames = [tkinter.PhotoImage(file=direc,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
    def update(ind):

        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        home.after(100, update, ind)
    label = tkinter.Label(home)
    label.pack()
    home.after(0, update, 0)

    home.mainloop()


#ADDING FIELD PAGE
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

        c.execute("INSERT INTO user_data_storage VALUES( :M_username, :url, :user_name, :service_pwd, :website_name)",
                {
                    'M_username': m_username,
                    'url':url,
                    'user_name': user_name,
                    'service_pwd': service_password,
                    'website_name': website_name,
                    
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

    home['bg']='black'
    home.title("The Bois Password Manager - Add A New Password")
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
#HOMEPAGE
def homePage():
    for widget in home.winfo_children():
        widget.destroy()
    
      
    def addPage():
        addField_Page()
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

loginPage()