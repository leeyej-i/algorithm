import sys
from collections import deque
M,N=map(int,sys.stdin.readline().split())
data=[]
queue=deque([])
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    for j in range(M):
        if data[i][j]==1 :
            queue.append([i,j])
def resolve_bps() :
    while queue:
        x,y=queue.popleft()
        if 0<=x-1<N and 0<=y<M and data[x-1][y]==0:
                queue.append([x-1,y])
                data[x-1][y] = data[x][y]+1
        if 0<=x+1<N and 0<=y<M and data[x+1][y]==0:
                queue.append([x+1,y])
                data[x+1][y] = data[x][y]+1
        if 0<=x<N and 0<=y-1<M and data[x][y-1]==0:
                queue.append([x,y-1])
                data[x][y-1] = data[x][y]+1
        if 0<=x<N and 0<=y+1<M and data[x][y+1]==0:
                queue.append([x,y+1])
                data[x][y+1] = data[x][y]+1
resolve_bps()
result=0
for i in data:
    for j in i:
        if j==0 :
            print(-1)
            exit(0) 
        result = max(result,j)
print(result-1)

             