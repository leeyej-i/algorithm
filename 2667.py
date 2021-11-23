import sys
from collections import deque
result=[]
N=int(sys.stdin.readline())
data=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def bfs_solve(i,k):
    queue = deque()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue.append((i,k))
    data[i][k]=0
    temp=1
    while(queue):
        x,y=queue.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<N and 0<=ny<N and data[nx][ny]==1 :
                data[nx][ny]=0
                queue.append((nx,ny))
                temp+=1
    return temp
                
for i in range(N):
    for k in range(N):
        if data[i][k] == 1 :
            result.append(bfs_solve(i,k))

print(len(result))
result.sort()
for item in result:
    print(item)