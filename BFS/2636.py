# 백준 2636
# 골드 4 / 치즈
from collections import deque
import sys

def bfs():
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append([0,0])
    visit[0][0] = 0
    meltCheck = 0
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<N and 0<=yy<M : 
                if visit[xx][yy] == -1:
                    if matrix[xx][yy] == 0 :
                        queue.append([xx,yy])
                        visit[xx][yy] = 0
                    elif matrix[xx][yy] == 1:
                        visit[xx][yy] = 0
                        matrix[xx][yy] = 0
                        meltCheck+=1
    return meltCheck
            
N,M = map(int,sys.stdin.readline().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,sys.stdin.readline().split())))
    
year = 0
result = 0
while True :
    visit= [[-1 for _ in range(M)] for _ in range(N)]
    bfsResult = bfs()
    if bfsResult > 0 :
        result = bfsResult
        year += 1
    else :
        break


print(year)
print(result)