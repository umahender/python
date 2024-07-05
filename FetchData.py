import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='userdata'
)
mycur=mydb.cursor()
query='select username,password from data'
mycur.execute(query)
result=mycur.fetchall()
for i in result:
    print(i)