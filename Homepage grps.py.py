import tkinter
import tkinter.font
def add():
    wim=tkinter.Tk()
    wim['bg']='black'
    wim.title("The Bois Password Manager")
    wim.geometry("920x640")
    Headin_text=tkinter.Label(wim,text="The Bois password manager",bg="black",fg="green")
    FontZ1=tkinter.font.Font(family="Ancient Modern Tales",size=64,)
    Headin_text.configure(font=FontZ1)
    Headin_text.pack()
    #url,username,password input
    url_text=tkinter.Label(wim,text="URL:",bg="black",fg="green")
    url_text.place(x=5,y=42)
    url_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    url_entry.place(x=50,y=42)

    usr_text=tkinter.Label(wim,text="Username:",bg="black",fg="green")
    usr_text.place(x=5,y=105)
    usr_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    usr_entry.place(x=90,y=105)

    pas_text=tkinter.Label(wim,text="Password:",bg="black",fg="green")
    pas_text.place(x=5,y=168)
    pas_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    pas_entry.place(x=120,y=168)

    pas_gen=tkinter.Button(wim,text="Password Generator",bg="black",fg="green",activebackground='#64f586')
    pas_gen.place(x=440,y=165)

    web_text=tkinter.Label(wim, text="Website name:",bg="black",fg="green")
    web_text.place(x=5,y=225)
    web_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    web_entry.place(x=150,y=225)
    
    wim.mainloop()