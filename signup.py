from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import mysql.connector
def login_page():
    swindow.destroy()
    import signin

def clear():
    emailEntry.delete(0,END)
    userNameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    cpasswordEntry.delete(0,END)
    check.set(0)
def connect_database():
    if emailEntry.get()=='' or userNameEntry.get()=='' or passwordEntry.get()=='' or cpasswordEntry.get()=='' :
        messagebox.showerror('error',"All field are required")
    elif passwordEntry.get()!=cpasswordEntry.get():
        messagebox.showerror('Error',"password mismatch")
    elif check.get()==0:
        messagebox.showerror('Error','please Accept Terams And condition')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error',"Database connectivity issue")
            return
        try:
            query='create database userdata'
            mycursor.execute(query)
            query='use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment,email varchar(50),username varchar(30),passord varchar(30))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='insert into data(email,username,password)values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),userNameEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('success','Registration is successfull')
        clear()
        swindow.destroy()
        import signin
swindow=Tk()
swindow.title("Signup Page")
swindow.resizable(False,False)
background=ImageTk.PhotoImage(file="bhag.jpg")
bglabel=Label(swindow,image=background)
bglabel.grid()

frame=Frame(swindow)
frame.place(x=640,y=100)
heading=Label(frame,text="CREATE ACCOUNT",font=('Microsoft YaHei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)
emaillabel=Label(frame,text="Email",font=('Microsoft YaHei UI Light',10,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0,sticky='w')
emailEntry=Entry(frame,width=20,font=('Microsoft YaHei UI Light',18,'bold'))
emailEntry.grid(row=2,column=0,sticky='w')
userNamelabel=Label(frame,text="UserName",font=('Microsoft YaHei UI Light',10,'bold'),bg='white',fg='firebrick1')
userNamelabel.grid(row=3,column=0,sticky='w')
userNameEntry=Entry(frame,width=20,font=('Microsoft YaHei UI Light',18,'bold'))
userNameEntry.grid(row=4,column=0,sticky='w')
passwordLabel=Label(frame,text="Password",font=('Microsoft YaHei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w')
passwordEntry=Entry(frame,width=20,font=('Microsoft YaHei UI Light',18,'bold'))
passwordEntry.grid(row=6,column=0,sticky='w')
cpasswordLabel=Label(frame,text="Confirm Password",font=('Microsoft YaHei UI Light',10,'bold'),bg='white',fg='firebrick1')
cpasswordLabel.grid(row=7,column=0,sticky='w')
cpasswordEntry=Entry(frame,width=20,font=('Microsoft YaHei UI Light',18,'bold'),fg='white',bg='firebrick1')
cpasswordEntry.grid(row=8,column=0,sticky='w')
check=IntVar()
terms=Checkbutton(frame,text='I agree to the terms & Conditions',font=('Microsoft YaHei UI Light',10,'bold'),fg='firebrick1',bg='white',variable=check)
terms.grid(row=9,column=0,padx=10)
butoon=Button(frame,text='Signup',font=('Microsoft YaHei UI Light',10,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',command=connect_database)
butoon.grid(row=10,column=0)
dontacc=Label(frame,text="Don't have an account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
dontacc.grid(row=11,column=0)
loginbutoon=Button(frame,text='Log in',font=('Microsoft YaHei UI Light',10,'bold underline'),bg='white',fg='blue',bd=0,cursor='hand2',activebackground='white',activeforeground='blue',command=login_page)
loginbutoon.grid(row=12,column=1)


swindow.mainloop()