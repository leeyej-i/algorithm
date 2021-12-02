# 백준 2468
# 실버 1 / 안전영역
import sys
from collections import deque
from copy import deepcopy
N=int(sys.stdin.readline())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
queue=deque()
def bfs(i,j):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    queue = deque()
    queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        graph_copy[x][y]=0
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<N and 0<=yy<N and graph_copy[xx][yy]!=0:
                queue.append((xx,yy))
                graph_copy[xx][yy]=0
result=[]
max_num=max(map(max,graph))
for i in range(max_num):
    result_item=0
    graph_copy=deepcopy(graph)
    for j in range(N):
        for k in range(N):
            if graph_copy[j][k] <= i :
                graph_copy[j][k]=0
    for j in range(N):
        for k in range(N):
            if graph_copy[j][k] !=0 :
                bfs(j,k)
                result_item+=1
    result.append(result_item)

print(max(result))