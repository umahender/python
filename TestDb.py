import dbm
#import pickle
import marshal
#f=open("data1.txt","rb")
#d=marshal.load(f)
'''f1=open("marsh.txt","rb")
data=marshal.load(f1)
exec(data)
print(data)
f1.close()

f=shelve.open("dtdb")
print(f['one'])'''
fp=dbm.open("testdb.db","r")
for k,v in fp.items():
    print(k,v)