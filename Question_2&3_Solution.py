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

double_check=True

while ball>0:
    ch = True
    print("Enter the direction in which the ball needs to travese:")
    dir = input()
    if dir=="ST":
        n_1=n-2
        while n_1>=0:
            if matrix[n_1][b]=="W":
                display(matrix,n,ball)
                break
            if matrix[n_1][b]>=1:
                matrix[n_1][b]=matrix[n_1][b]-1
                display(matrix,n,ball)
                break
            n_1-=1
    elif dir=="LD":
        if matrix[n-1][b-1]=="W":
            che=True
            for e in range(1,n-1):
                if matrix[n-2][e]>=1:
                    matrix[n - 2][e] =matrix[n - 2][e]-1
                    matrix[n-1][e]="o"
                    matrix[n-1][b]="G"
                    che=False
                    if e!=b:
                        ball-=1
                    display(matrix, n, ball)
                    break
            if che:
                b-=1
                matrix[n - 1][b]="G"
                matrix[n-1][(n-1)//2]="o"
                b=(n-1)//2
                display(matrix, n, ball)
        else:
            matrix[n-1][b-1]="o"
            matrix[n-1][b]="G"
            ball-=1
            b=b-1
            n_1 = n - 2
            while n_1 >= 0:
                if matrix[n_1][b] >= 1:
                    matrix[n_1][b] = matrix[n_1][b]-1
                    display(matrix, n, ball)
                    break
                if matrix[n_1][b] == "W":
                    display(matrix, n, ball)
                    break
                n_1-=1
    elif dir=="RD":
        if matrix[n-1][b+1]=="W":
            checking=True
            for e in range(n-1,0,-1):
                if matrix[n-2][e]>=1:
                    matrix[n - 2][e] =matrix[n - 2][e]-1
                    matrix[n-1][e]="o"
                    matrix[n-1][b]="G"
                    checking=False
                    if e!=b:
                        ball-=1
                    display(matrix, n, ball)
                    break
            if checking:
                b-=1
                matrix[n - 1][b]="G"
                matrix[n-1][(n-1)//2]="o"
                b=(n-1)//2
                display(matrix, n, ball)
        else:
            matrix[n-1][b+1]="o"
            matrix[n-1][b]="G"
            ball-=1
            b=b+1
            n_1 = n - 2
            while n_1 >= 0:
                if matrix[n_1][b] >= 1:
                    matrix[n_1][b] = matrix[n_1][b]-1
                    display(matrix, n, ball)
                    break
                if matrix[n_1][b] == "W":
                    display(matrix, n, ball)
                    break
                n_1-=1
    for iter in matrix:
        if 1 in iter:
            ch=False
    if ch:
        double_check=False
        print("You Win Hurray")
        break

check=True
for iter in matrix:
    if 1 in iter and ball==0:
        print("game over")
        check=False
        break
if check and double_check:
    print("You Win Hurray")
