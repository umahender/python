from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("1370x700+0+0")
win.title("Student informaation")
headtitle = Label(win,text="Welcome",font=("Arial",24,"bold"),bg="#008080",fg="white")
headtitle.pack(side=TOP,fill='x',pady=40)
# left side part
fr = Frame(win,bg="lightgrey",bd="12")
fr.place(x=10,y=100,height=700,width=800)

ti = Label(fr,text="Enter-Data",font=("Arial",24,"bold"),bg="red",fg="white")
ti.pack(side=TOP,fill='x',pady=0)
# right side part
rightfr = Frame(win,bg="lightgrey",bd="12")
rightfr.place(x=810,y=100,height=700,width=800)

righttitle = Label(rightfr,text="Search-Data",font=("Arial",24,"bold"),bg="red",fg="white")
righttitle.pack(side=TOP,fill='x',pady=0)






win.mainloop()

