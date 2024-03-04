
import mysql.connector

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pythonp'
)
curs=conn.cursor();

curs.execute("insert into pg values('mahender')")
curs.execute("select *from pg")
print(curs.fetchall())
conn.commit()