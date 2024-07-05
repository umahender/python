import pickle
f=open("data12345.txt","wb")
dct={"name":"Ravi","Age":23,"gender":"M"}
lis=[1,2,3,4]
pickle.dump(dct,f)
pickle.dump(lis,f)
f.close()