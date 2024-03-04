from tkinter import *;
root=Tk()
root.geometry("1040x650")
labelhead=Label(root,text="Sign in form",font=('times new roman' ,30 ,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
labelhead.pack(fill=X)
customer_detail_frame=LabelFrame(root,text='customer details' ,font=('times new roman' ,15 ,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
customer_detail_frame.pack()
labelname=Label(customer_detail_frame,text='Name',font=('times new roman' ,18 ,'bold'),bg='gray20',fg='gold')
labelname.grid(row=0,column=0)
nameEntry=Entry(customer_detail_frame)
nameEntry.grid(row=0,column=1)


root.mainloop();