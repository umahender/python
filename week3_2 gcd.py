def gcd(a,b):
    while(b>0):
        r=a%b
        a=b
        b=r
    return a

a=int(input("Enter the first number"))
b=int(input("Enter the first number"))

if(a<b):
    temp=a
    a=b
    b=temp
print('gcd of ',gcd(a,b))

