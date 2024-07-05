import mysql.connector
mydb=mysql.connector.connect(host='localhost',username='root',password='',database='demodb')
curs=mydb.cursor()

#curs.execute("create database demodb")
#curs.execute("create table data(name varchar(30),email varchar(50),password varchar(50))")
#curs.execute("use demodb")
#curs.execute("show tables")
#sql="INSERT INTO DATA(name,email,password)values(%s,%s,%s)"
#val=("mahender","mahender@gmail.com","2345")
#curs.execute(sql,val)
#mydb.commit()
curs.execute("select *from data")
for x in curs:
    print(x)