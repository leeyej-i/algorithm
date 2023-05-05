# 백준 4963
# 실버 2 / 섬의 개수
import sys
from collections import deque

def bfs(i,j):
    dx=[1,-1,0,0,1,-1,1,-1]
    dy=[0,0,1,-1,1,-1,-1,1]
    queue = deque()
    queue.append((i,j))
    while queue:
        x,y=queue.popleft()
        for k in range(8):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<h and 0<=yy<w and graph[xx][yy]==1:
                queue.append((xx,yy))
                graph[xx][yy]=0

while True:
    w,h=map(int,sys.stdin.readline().split())
    if w==0 and h==0 :
        break
    graph=[]
    queue=deque()
    result=0
    for i in range(h):
        data=list(map(int,sys.stdin.readline().split()))
        graph.append(data)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 :
                bfs(i,j)
                result+=1
    print(result)



                
        
    