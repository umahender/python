def invert(dic):
    invert_dic={v:k for k,v in dic.items()}
    return invert_dic
dic_items={}
num_ent=int(input("Enter number of entry"))
for i in range(num_ent):
    key=input("Enter key ")
    value=input("Enter value")
    dic_items[key]=value
print(dic_items)
print("after invert")
print(invert(dic_items))