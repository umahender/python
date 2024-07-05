def read_mat(mat,r,c):
    for i in range(r):
        matrix=[]
        for j in range(c):
            val=int(input(f"Enter the matrix[{i}][{j}] value"))
            matrix.append(val)
        mat.append(matrix)
def disp_mat(mat):
    for i in mat:
        print(i)


r=int(input("Enter no of rows" ))
c=int(input("Enter no of columns" ))
A=[]
#read mat
read_mat(A,r,c)
disp_mat(A)
r1=int(input("Enter no of rows" ))
c1=int(input("Enter no of columns" ))
B=[]
#read mat
read_mat(B,r,c)
disp_mat(B)
C=[]
for i in range(r):
    t=[]
    for j in range(c):
        val=A[i][j]+B[i][j]
        t.append(val)
    C.append(t)

D=[]
for i in range(r):
    t=[]

    for j in range(c1):
        sum=0
        for k in range(r1):            sum=sum+A[i][k]*B[k][j]
            t.append(sum)
        D[i].append(t)

#print(C)
print("Resultant Matrix")
disp_mat(D)