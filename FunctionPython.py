r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))
A=[]
for i in range(r):
    x=[]
    for j in range(c):
        x.append(int(input("Enter the elements")))
    A.append(x)

for x in A:
    print(x)
