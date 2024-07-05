import marshal
scr="""
a=10
b=20
print("Addition= ",a+b)
"""
code=compile(scr,"scr","exec")
f1=open("marsh.txt","wb")
marshal.dump(code,f1)