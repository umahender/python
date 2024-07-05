import shelve
with shelve.open("test1")as db:
    db['abc']=1
    db['maeh']=2
s=shelve.open('dtdb')
s['one']=1
s['two']=2
db.close()