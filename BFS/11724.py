import sys
from collections import deque
N,M=map(int, sys.stdin.readline().split())
graph=[[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,sys.stdin.readline().split())
    graph[x][y]=graph[y][x]=1
visit=[]

def bfs(i) :
    queue=deque()
    queue.append(i)
    visit.append(i)
    while queue:
        x=queue.popleft()
        for j in range(1,N+1):
            if j not in visit and graph[x][j]==1:
                queue.append(j)
                visit.append(j)
temp=0
for i in range(1,N+1):
    if i not in visit:
        bfs(i)
        temp+=1

print(temp)