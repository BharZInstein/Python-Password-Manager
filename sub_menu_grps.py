from tkinter import *
def add():
    wim=Tk()
    wim.title("The Bois Password Manager")
    wim.geometry("920x640")
    Headin_text=Label(wim,text="The Bois password manager Add Password")
    Headin_text.pack()
    #url,username,password input
    url_text=Label(wim,text="URL:")
    url_text.place(x=5,y=42)
    url_entry=Entry(wim,width=50)
    url_entry.place(x=50,y=42)

    usr_text=Label(wim,text="Username:")
    usr_text.place(x=5,y=105)
    usr_entry=Entry(wim,width=50)
    usr_entry.place(x=90,y=105)

    pas_text=Label(wim,text="Password:")
    pas_text.place(x=5,y=168)
    pas_entry=Entry(wim,width=50)
    pas_entry.place(x=120,y=168)

    pas_gen=Button(wim,text="Password Generator")
    pas_gen.place(x=440,y=165)

    web_text=Label(wim, text="Website name:")
    web_text.place(x=5,y=225)
    web_entry=Entry(wim,width=50)
    web_entry.place(x=150,y=225)
    
    wim.mainloop()