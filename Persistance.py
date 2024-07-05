import pickleDemo
import marshal
import shelve
import dbm
mylist=[1,"hi",2,"hello"]
with open("abc24.txt",'wb') as a:
    pickle.dump(mylist,a)
with open('abc24.txt','rb') as m:
    m2=pickle.loads(m)
print(m)