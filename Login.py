from tkinter import*
from  PIL import ImageTk
from tkinter import messagebox
import mysql.connector
def saveData():
    if (usernameEntry.get() == '' or emailEntry.get() == '' or passwordEntry.get() == ''):
        messagebox.showerror('Error', "All fields are mandotary")
    else:
        try:
            conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='userdata'
            )
            mycursor=conn.cursor()
            sql='insert into student12(username,email,password)values(%s,%s,%s)'
            mycursor.execute(sql,(usernameEntry.get(),emailEntry.get(),passwordEntry.get()))
            conn.commit()
            messagebox.showinfo('success'," Data saved successfully")


        except:
            messagebox.showerror('Error','Problem in database connection')


window=Tk()
background=ImageTk.PhotoImage(file='azad.jpg')
blabel=Label(window,image=background)
blabel.grid()
frame=Frame(window)
frame.place(x=600,y=100)
usernamelabel=Label(frame,text="UserName",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
usernamelabel.grid(row=0,column=0)
usernameEntry=Entry(frame,width=29)
usernameEntry.grid(row=0,column=1)
emaillabel=Label(frame,text="Email",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0)
emailEntry=Entry(frame,width=29)
emailEntry.grid(row=1,column=1)
passwordlabel=Label(frame,text="Password",font=('Arial',15,'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=2,column=0)
passwordEntry=Entry(frame,width=29)
passwordEntry.grid(row=2,column=1)
button=Button(frame,text="Save" ,command=saveData)
button.grid(row=3,column=1)





window.mainloop()