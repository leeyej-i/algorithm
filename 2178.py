import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
data=[]
visit=[]
queue=deque()
for i in range(N):
    str=list(sys.stdin.readline().strip())
    data.append(list(map(int,str)))
queue.append([0,0])
def resolve_bfs() :
    while queue:
        x,y=queue.popleft()
        visit.append([x,y])
        if 0<=x-1<N and 0<=y<M and data[x-1][y]==1 :
           if [x-1,y] not in visit:
                queue.append([x-1,y])
                visit.append([x-1,y])
                data[x-1][y] = data[x][y]+1
        if 0<=x+1<N and 0<=y<M and data[x+1][y]==1:
            if [x+1,y] not in visit:
                queue.append([x+1,y])
                visit.append([x+1,y])
                data[x+1][y] = data[x][y]+1
        if 0<=x<N and 0<=y-1<M and data[x][y-1]==1:
            if [x,y-1] not in visit:
                queue.append([x,y-1])
                visit.append([x,y-1])
                data[x][y-1] = data[x][y]+1
        if 0<=x<N and 0<=y+1<M and data[x][y+1]==1 :
            if [x,y+1] not in visit:
                queue.append([x,y+1])
                visit.append([x,y+1])
                data[x][y+1] = data[x][y]+1
resolve_bfs()
print(data[N-1][M-1])

             