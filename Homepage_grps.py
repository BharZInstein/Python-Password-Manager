import tkinter
import tkinter.font
import random
import pyperclip
import string




def add():
    '''def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        password_list = password_letters + password_numbers + password_symbols
        random.shuffle(password_list)
        password = "".join(password_list)

        pas_entry.insert(0, password)
        pyperclip.copy(password)'''
    def randpass():
        length = 10
        small = string.ascii_lowercase 
        big = string.ascii_uppercase
        dig = string.digits
        symbols = string.punctuation

        all = small + big + dig + symbols

        Pass = random.sample(all,length)

        password = "".join(Pass)
        pas_entry.insert(0, password)
        pyperclip.copy(password)
    
    wim=tkinter.Tk()
    wim['bg']='black'
    wim.title("The Bois Password Manager")
    wim.geometry("920x640")
    Headin_text=tkinter.Label(wim,text="The Bois password manager",bg="black",fg="green")
    Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                 size = 25, 
                                 )
    Headin_text.configure(font=Custom_Font)
    Headin_text.pack()
    #url,username,password input
    url_text=tkinter.Label(wim,text="URL:",bg="black",fg="green")
    url_text.place(x=5,y=42)
    url_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    url_entry.place(x=150,y=42)

    usr_text=tkinter.Label(wim,text="Username:",bg="black",fg="green")
    usr_text.place(x=5,y=105)
    usr_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    usr_entry.place(x=150,y=105)

    pas_text=tkinter.Label(wim,text="Password:",bg="black",fg="green")
    pas_text.place(x=5,y=168)
    pas_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    pas_entry.place(x=150,y=168)
    pas_gen=tkinter.Button(wim,text="Password Generator",bg="black",fg="green",activebackground='#64f586', command=randpass)
    pas_gen.place(x=460,y=165)

    web_text=tkinter.Label(wim, text="Website name:",bg="black",fg="green")
    web_text.place(x=5,y=225)
    web_entry=tkinter.Entry(wim,width=50,fg="black", bg="#64f586")
    web_entry.place(x=150,y=225)
    Go_Button=tkinter.Button(wim,text="GO",bg="#00ff95",fg="green",width=25,height=2,activebackground='#64f586')
    Go_Button.place(x=150,y=275)
    
    

    wim.mainloop()