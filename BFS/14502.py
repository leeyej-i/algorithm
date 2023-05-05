# 백준 14502
# 골드 5 / 연구소
from collections import deque
from copy import deepcopy
import sys

def bfs():
    data2 = deepcopy(data)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue=deque([])
    for i in range(N):
        for j in range(M):
            if data2[i][j] == 2 :
                queue.append([i,j])
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx <= N-1 and 0<=yy<=M-1 :
                if data2[xx][yy]==0:
                    queue.append([xx,yy])
                    data2[xx][yy] = 2
    result = 0
    for i in range(N):
        for j in range(M):
            if data2[i][j] == 0 :
                result+=1
    return result

def back_func(cnt):
    global res
    if cnt == 3:
        res = max(res,bfs())
        return
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                 data[i][j] = 1
                 back_func(cnt+1)
                 data[i][j] = 0
        
N,M = map(int,sys.stdin.readline().split())
data = []
res = 0

for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
back_func(0)
print(res)