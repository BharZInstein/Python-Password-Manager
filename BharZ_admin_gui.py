#Read the readme.txt file before running IMPORTANT
import tkinter
import tkinter.font
from tkinter import messagebox
import sqlite3
from functools import partial
username=None
password=None
#delete butoon function
def delete_data(username):
    conn = sqlite3.connect('pass_manager.db')
    c = conn.cursor()
    c.execute("DELETE FROM user_data WHERE M_username=?", (username,))
    conn.commit()
    conn.close()
    
    admin_view_page()
    return None

#username view
def view_db():
    Entry_Font=tkinter.font.Font(size=15)
    conn = sqlite3.connect('pass_manager.db')
    c = conn.cursor()
    c.execute("SELECT * FROM user_data")
    rows=c.fetchall()
    if (rows!=[]):
        i=0
        y=0
        while True:
            c.execute("SELECT * FROM user_data")
            array=c.fetchall()

            lbl=tkinter.Label(win,text=(array[i][0]),bg="#000000", fg='green',activebackground='#64f586')
            lbl.config(font=Entry_Font)
            lbl.place(x=30,y=y+80)

            delbt=tkinter.Button(win,text='Delete',bg="#000000", fg='green',activebackground='#64f586',command= partial(delete_data, array[i][0]))
            delbt.place(x=200,y=y+80)
            i=i+1
            y=y+35

            c.execute("SELECT * FROM user_data")
            array=c.fetchall()
            if len(array) <=i:
                break
        
    conn.close()
    return None

#Main GUI
win=tkinter.Tk()
win.title("Admin Portal")
win.geometry("918x450")
Entry_Font=tkinter.font.Font(size=15)
icon= tkinter.PhotoImage(file="images\icon_2.png")
win.iconphoto(False, icon)
#admin page GUI
def admin_page():
    for widget in win.winfo_children():
        widget.destroy()
    def admin_login():
        global username
        global password
        username=entry1.get()
        password=entry2.get()
        conn = sqlite3.connect('pass_manager.db')
        c = conn.cursor()
        c.execute("SELECT * from admin_user_data WHERE admin_username=? AND admin_pwd=?", (username,password,))
        rows=c.fetchall()
        if rows==[]:
            wrg=tkinter.Label(win,text="*Wrong Username/Password",fg="red",bg="black")
            wrg.place(x=500,y=134)
            entry1.delete(0, 'end')
            entry2.delete(0, 'end')
        else:
            admin_view_page()
        conn.close()

    win['bg']='black'
    Headin_text=tkinter.Label(text="Admin Login Portal",
    fg="green",bg="black")
    Headin_text.pack()
    Custom_Font=tkinter.font.Font( family = "Ancient Modern tales", 
                                    size = 25, 
                                    )
    Headin_text.configure(font=Custom_Font)
    text1=tkinter.Label(win,text="Admin Username:",fg="green",bg="black")
    Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
    text1.configure(font=Custom_Font1)
    text1.pack(pady=20,side=tkinter.TOP,anchor="w")
    entry1 = tkinter.Entry(fg="black", bg="#64f586", width=50)
    entry1.place(x=172,y=68)

    text2=tkinter.Label(win,text="Admin Password:",fg="green",bg="black")
    text2.pack(pady=20,side=tkinter.TOP,anchor="w")
    text2.configure(font=Custom_Font1)
    entry2=tkinter.Entry(win,show="*",fg="black", bg="#64f586", width=50)
    entry2.place(x=172,y=134)
    credit=tkinter.Label(win,text="©️Created by Kanish, Bharghav, Seyan, Adhiraj",fg="grey",bg="black")
    credit.place(x=650,y=429)
    Login_button= tkinter.Button(
        text="Login",
        width=10,
        height=2,
        bg="#61ff96",
        fg="black",
        command=admin_login
    )
    Login_button.pack()

    label = tkinter.Label(win)



    win.mainloop()

#Admin View Page
def admin_view_page():
    for widget in win.winfo_children():
        widget.destroy()
    win.geometry("600x750")
    win.title("The Bois Password Manager - Admin Pannel")
    Headin_text=tkinter.Label(win,text="Admin Pannel - Customer ID",bg="black",fg="green")
    Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                    size = 25, 
                                    )
    Entry_Font=tkinter.font.Font(size=15)  
    Grid_hed_Font=tkinter.font.Font(family = "Pixeboy",size=25)                         
    Headin_text.configure(font=Custom_Font)
    Headin_text.pack()

    web_grid_sh=tkinter.Label(win,text='CUSTOMER USERNAMES', fg='green', bg='black')
    web_grid_sh.config(font=Grid_hed_Font)
    web_grid_sh.place(x=30,y=50)
    logout=tkinter.Button(win,text="Logout",bg="black",fg="green",activebackground='#64f586',command=admin_page)
    logout.place(y=5, x=550)
    credit=tkinter.Label(win,text="©️Created by Kanish, Bharghav, Seyan, Adhiraj",fg="grey",bg="black")
    credit.place(x=332,y=729)
    view_db()

    win.mainloop()

admin_page()