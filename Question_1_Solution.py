print("Enter size of the NxN matrix:")
n=int(input())
l=[]
c="Y"
while c=="Y":
    print("Enter the brick's position and the brick type:")
    l.append(list(map(int,input().split())))
    print("Do you want to continue(Y or N)?")
    c=input()
print("Enter ball Count")
ball=int(input())
matrix=[]
index=0

def display(matrix,n,ball):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                print(end=" ")
            else:
                print(matrix[i][j], end="")
            print(end=" ")
        print("")
    print("Ball count is", ball)

for i in range(n):
    row=[]
    for j in range(n):
        checker=True
        if i==0 or j==0 or j==(n-1):
            row.append("W")
            checker=False
        elif i==(n-1) and (j!=0 or j!=(n-1)) and j!=(n-1)//2:
            row.append("G")
            checker = False
        elif i==(n-1) and j==(n-1)//2:
            row.append("o")
            b=j
            checker = False
        for k in l:
            if i==k[0] and j==k[1]:
                row.append(l[index][2])
                index+=1
                checker = False
                break
        if checker:
            row.append(0)
    matrix.append(row)

display(matrix, n, ball)
