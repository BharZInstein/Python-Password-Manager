#GUI FOR CSC PROJECT by Bharghav
import tkinter
import tkinter.font
win=tkinter.Tk()
win.title("The Bois Password Manager")
win.geometry("918x450")
win['bg']='black'
Headin_text=tkinter.Label(text="The Bois password manager Login Portal",
fg="green",bg="black")
Headin_text.pack()
Custom_Font=tkinter.font.Font( family = "Pixeboy", 
                                 size = 25, 
                                 )
Headin_text.configure(font=Custom_Font)
text1=tkinter.Label(win,text="Username:",fg="green",bg="black")
Custom_Font1=tkinter.font.Font(family="Consolas",size=15)
text1.configure(font=Custom_Font1)
text1.pack(pady=20,side=tkinter.TOP,anchor="w")
entry1 = tkinter.Entry(fg="black", bg="#64f586", width=50)
entry1.place(x=100,y=50)

text2=tkinter.Label(win,text="Master Password:",fg="green",bg="black")
text2.pack(pady=20,side=tkinter.TOP,anchor="w")
text2.configure(font=Custom_Font1)
entry2=tkinter.Entry(fg="black", bg="#64f586", width=50)
entry2.place(x=180,y=120)
Username=entry1.get()
Password=entry2.get()
Login_button= tkinter.Button(
    text="Login",
    width=10,
    height=2,
    bg="#61ff96",
    fg="black",
)
Login_button.pack()


win.mainloop()


