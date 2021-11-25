import sys
from collections import deque
N=int(sys.stdin.readline())
visit=[]
queue=deque()
result=[]
graph=[[0]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    x,y=map(int, sys.stdin.readline().split())
    graph[x][y]=graph[y][x]=1
    if graph[1][x]==1 :
        queue.append((1,x))
        visit.append(1)
        result.append([1,y])
    elif graph[1][y] ==1 :
        queue.append((1,y))
        visit.append(1)
        result.append([1,y])

while queue :
    xp,yp=queue.popleft()
    for i in range(1,N+1):
        if graph[yp][i]==1 and i is not visit:
            queue.append((yp,i))
            visit.append(yp)
            result.append([yp,i])

print(result)
            
        
    
