import marshal
import shelve
fp=open("marsh1.txt","rb")
data=marshal.load(fp)
exec (data)
fp=shelve.open("shelve")
print(list(fp.keys()))