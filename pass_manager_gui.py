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
from functools import partial
M_password=None
M_username=None
url=None
usr=None
website_name=None
m_username=None
username=None
password=None
search=None
#search data
def search_db(m_username,website_name):
    Entry_Font=tkinter.font.Font(size=15)
    conn = sqlite3.connect('pass_manager.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_data_storage WHERE M_username=? AND website_name=? ", (m_username,website_name,))
    rows=c.fetchall()
    if (rows!=[]):
        i=0
        y=0
        while True:
            c.execute("SELECT * FROM user_data_storage WHERE M_username=? AND website_name=? ", (m_username,website_name,))
            array=c.fetchall()

            lbl=tkinter.Label(home,text=(array[i][4]),bg="#000000", fg='green',activebackground='#64f586')
            lbl.config(font=Entry_Font)
            lbl.place(x=88,y=y+199)
            lbl=tkinter.Label(home,text=(array[i][2]),bg="#000000", fg='green',activebackground='#64f586')
            lbl.config(font=Entry_Font)
            lbl.place(x=378,y=y+190)
            lbl=tkinter.Label(home,text=(array[i][3]),bg="#000000", fg='green',activebackground='#64f586')
            lbl.config(font=Entry_Font)
            lbl.place(x=650,y=y+190)

            delbt=tkinter.Button(home,text='Delete',bg="#000000", fg='green',activebackground='#64f586',command= partial(delete_data, array[i][0], array[0][2],array[0][3],array[0][4]))
            delbt.place(x=870,y=y+190)
            i=i+1
            y=y+50

            c.execute("SELECT * FROM user_data_storage WHERE M_username=? AND website_name=? ", (m_username,website_name,))
            array=c.fetchall()
            if len(array) <=i:
                break
    else:
        ln=tkinter.Label(home,text="*No Entry Found",fg="red",bg="black")
        ln.place(y=63,x=600)
        
    conn.close()
    return None

#delete function
def delete_data(M_username,username,password,website):
    conn = sqlite3.connect('pass_manager.db')
    c = conn.cursor()
    c.execute("DELETE FROM user_data_storage WHERE M_username=? AND user_name=? AND service_pwd=? AND website_name=?", (M_username,username,password,website))
    conn.commit()
    conn.close()
    
    search_GUI()
    return None

#signUp DB
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
    

#GUI STARTS HERE
#main UI
home=tkinter.Tk()
home.title("The Bois Password Manager")
home.geometry("920x640")
icon= tkinter.PhotoImage(file="images\icon_2.png")
home.iconphoto(False, icon)
Entry_Font=tkinter.font.Font(size=15)

#signUP GUI
def signUp_Command():
    def signUp_contets():
        global M_username
        global M_password
        M_username=user_name_entry.get()
        M_password=pass_word_entry.get()
        if (len(M_password)==0 or len(M_username)==0):
            ln=tkinter.Label(root,text="*Enter a username/password",fg="red",bg="black")
            ln.pack()
        else:
            try:
                M_password=make_pw_hash(M_password)
                signUp(M_username,M_password)
                en=tkinter.Label(root,text="*Account Created Successfully",fg="red",bg="black")
                en.pack()
            except sqlite3.IntegrityError:
                ln=tkinter.Label(root,text="*Username already exists",fg="red",bg="black")
                ln.pack()
                
        return None
    root=tkinter.Tk()
    root.title("The Bois Password Manager - SignUp")
    root.geometry("500x200")
    root['bg']='black'
    Headin_text=tkinter.Label(root,text="SignUp",
    fg="green",bg="black")
    Font23=Custom_Font1=tkinter.font.Font(family="Pixeboy",size=25)
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
    welcomeusername=user_name_entry.get()
    user_name_entry.pack()

    pass_word=tkinter.Label(root,text="Master Password:",fg="green",bg="black")
    pass_word.pack()
    pass_word.configure(font=Custom_Font1)
    pass_word_entry=tkinter.Entry(root,show="*",fg="black", bg="#64f586", width=50)
    pass_word_entry.pack()
    signUp_button= tkinter.Button(root,text="SignUp",width=10,height=2,bg="#61ff96",fg="black",command = signUp_contets)
    signUp_button.pack(pady=5)
    root.mainloop()

#login GUI
def loginPage():
    for widget in home.winfo_children():
        widget.destroy()
    #Login Main
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
    '''direc="images\matrix.gif"
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
    home.after(0, update, 0)'''

    home.mainloop()

#HOMEPAGE GUI
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
    welcome_text=tkinter.Label(home,text="Welcome👋",bg="black",fg="green")
    Font111=tkinter.font.Font(home,family="Pixeboy",size=30)
    welcome_text.configure(font=Font111)
    welcome_text.pack()
    userZ_text=tkinter.Label(home,text=m_username,bg="black",fg="#3a17ff")
    CustomFont131=tkinter.font.Font(home,family="Comic Sans MS",size=28)
    userZ_text.configure(font=CustomFont131)
    userZ_text.pack()
    Headin_text=tkinter.Label(home,text="----Choose an Option----",bg="black",fg="green")
    Custom_Font2=tkinter.font.Font(family="Consolas",size=14,weight="bold")
    Headin_text.configure(font=Custom_Font2)
    Headin_text.pack()
    add=tkinter.Button(home,text="Add new Password",width=20,height=2, bg="black",fg="green", activebackground='#64f586',command=addPage)
    add.pack(pady=20)
    see=tkinter.Button(home,text="View your passwords", width=20, height=2,bg="black",fg="green", activebackground='#64f586')
    see.pack()
    search=tkinter.Button(home,text="Search your passwords", width=20, height=2,bg="black",fg="green", activebackground='#64f586', command=search_GUI)
    search.pack(pady=20)
    logout=tkinter.Button(home,text="Logout",bg="black",fg="green",activebackground='#64f586',command=loginPage)
    logout.place(y=5, x=865)
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
    Go_Button=tkinter.Button(home,text="ADD",bg="#000000",fg="green",width=25,height=2,activebackground='#64f586', command=addEntry)
    Go_Button.place(x=150,y=275)
    back=tkinter.Button(home,text='Back',bg="#000000", fg='green',activebackground='#64f586',command=homePage)
    back.place(x=3,y=3)
    logout=tkinter.Button(home,text="Logout",bg="black",fg="green",activebackground='#64f586',command=loginPage)
    logout.place(y=5, x=865)

    home.mainloop()

#Search GUI
def search_GUI():
    for widget in home.winfo_children():
        widget.destroy()
    
    def serach_Entry():
        global search
        search=webs_name_entry.get()
        if len(search)!=0:
            search_db(m_username, search)
        else:
            ln=tkinter.Label(home,text="*Fill the search box",fg="red",bg="black")
            ln.place(y=63,x=600)
        return None
    home['bg']='black'
    home.title("The Bois Password Manager - Search A Password")
    Headin_text=tkinter.Label(home,text="The Bois password manager",bg="black",fg="green")
    Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
    Entry_Font=tkinter.font.Font(size=15)  
    Grid_hed_Font=tkinter.font.Font(family = "Pixeboy",size=25)                         
    Headin_text.configure(font=Custom_Font)
    Headin_text.pack()
    back=tkinter.Button(home,text='Back',bg="#000000", fg='green',activebackground='#64f586',command=homePage)
    back.place(x=3,y=3)
    webs_name=tkinter.Label(home,text='Enter The Website Name:', fg='green', bg='black')
    webs_name.config(font=Entry_Font)
    webs_name.place(x=5, y=60)
    webs_name_entry=tkinter.Entry(home,width=40,fg="black", bg="#64f586")
    webs_name_entry.place(y=65, x=250)
    search_btn=tkinter.Button(home,text='Search',bg="#000000", fg='green',activebackground='#64f586', command=serach_Entry)
    search_btn.place(y=63,x=500)
    #search grid
    web_grid_sh=tkinter.Label(home,text='Website', fg='green', bg='black')
    web_grid_sh.config(font=Grid_hed_Font)
    web_grid_sh.place(x=80,y=130)
    usr_grid_sh=tkinter.Label(home,text='Username', fg='green', bg='black')
    usr_grid_sh.config(font=Grid_hed_Font)
    usr_grid_sh.place(x=370,y=130)
    pas_grid_sh=tkinter.Label(home,text='Password', fg='green', bg='black')
    pas_grid_sh.config(font=Grid_hed_Font)
    pas_grid_sh.place(x=670,y=130)
    logout=tkinter.Button(home,text="Logout",bg="black",fg="green",activebackground='#64f586',command=loginPage)
    logout.place(y=5, x=865)

    home.mainloop()


    
loginPage()