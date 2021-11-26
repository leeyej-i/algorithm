# 백준 18405
# 실버 1 / 경쟁적 전염
import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())
data=[]
q=[]
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        if data[i][j]!=0:
            q.append((data[i][j],i,j))
S,X,Y=map(int,sys.stdin.readline().split())
q.sort()
queue=deque(q)

dx=[1,-1,0,0]
dy=[0,0,-1,1]
time=0
while queue :
    if time == S:
        break
    for _ in range(len(queue)):
        value,xx,yy = queue.popleft()
        for i in range(4):
            dxx=xx+dx[i]
            dyy=yy+dy[i]
            if 0<=dxx<N and 0<=dyy<N and data[dxx][dyy]==0:
                data[dxx][dyy]=data[xx][yy]
                queue.append((data[xx][yy],dxx,dyy))
    time+=1
    
print(data[X-1][Y-1])