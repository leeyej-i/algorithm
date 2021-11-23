import sys
from collections import deque
T=int(sys.stdin.readline())
for _ in range(T):
    M,N,K=map(int,sys.stdin.readline().split())
    data=[]
    for i in range(N):
        line = []
        for j in range(M):
            line.append(0)
        data.append(line)
    for i in range(K):
        x,y = map(int,sys.stdin.readline().split())
        data[y][x]=1
    
    def bfs_resolve(i,j) :
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        queue = deque()
        queue.append((i,j))
        while queue :
            x,y = queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<N and 0<=ny<M :
                    if data[nx][ny]==1:
                        data[nx][ny]=0
                        queue.append((nx,ny))
    
    temp=0        
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 :
                bfs_resolve(i,j)
                temp+=1
    print(temp)            