import sys
N,K=map(int,sys.stdin.readline().split())
data=[]
result=0
for i in range(N):
    data.append(int(sys.stdin.readline().strip()))
for i in range(N-1, -1, -1):
    if K//data[i] > 0 :
        result+=K//data[i]
        K=K-(K//data[i])*data[i]
print(result)