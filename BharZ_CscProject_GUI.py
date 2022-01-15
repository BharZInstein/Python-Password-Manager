#GUI FOR CSC PROJECT by Bharghav
import tkinter
import tkinter.font
win=tkinter.Tk()
win.title("The Bois Password Manager")
win.geometry("920x640")
win['bg']='black'
icon= tkinter.PhotoImage(file="images\icon_2.png")
win.iconphoto(False, icon)
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
entry2=tkinter.Entry(show="*",fg="black", bg="#64f586", width=50)
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
direc="images\matrix.gif"
Login_button.pack()
frameCnt = 20
frames = [tkinter.PhotoImage(file=direc,format = 'gif -index %i' %(i)) for i in range(frameCnt)]
def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    win.after(100, update, ind)
label = tkinter.Label(win)
label.pack()
win.after(0, update, 0)

win.mainloop()