import sys
N=int(sys.stdin.readline())
data=[[0 for i in range(10)]for _ in range(2)]
for i in range(1,10):
    data[0][i]=1
    
for _ in range(1,N):
    for j in range(10):
        if j==0:
            data[1][j]=data[0][j+1]
        elif j== 9:
            data[1][j]=data[0][j-1]
        else :
            data[1][j]=data[0][j-1]+data[0][j+1]
    for j in range(10):
        data[0][j]=data[1][j]
        
if N==1 : 
    print(sum(data[0]))
else :
    print(sum(data[1])%1000000000)