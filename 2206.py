# 백준 2206
# 골드 4 / 벽 부수고 이동하기
from collections import deque
import sys

def bfs() :
    start = [0,0,1,0] #x, y, cost, check
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque([start])
    queue2 = deque([start])
    data[0][0] = '2'
    while queue :
        x,y,cost,check = queue.popleft()
        if x == N-1 and y == M-1:
            return cost
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<N and 0<=yy<M:
                if check == 0 :
                    if data[xx][yy] == '0' :
                        queue.append([xx,yy,cost+1,check])
                        data[xx][yy] = '2' #벽안부수고 가기
                    if data[xx][yy] == '1' :
                        queue.append([xx,yy,cost+1,1])
                    if data[xx][yy] == '3' :
                        queue.append([xx,yy,cost+1,check])
                        data[xx][yy] = '2' #벽안부순걸로 치기
                else :
                    if data[xx][yy] == '0' :
                        queue.append([xx,yy,cost+1,check])
                        data[xx][yy] = '3' #벽부수고 간 곳
                    else :
                        continue
    return -1
N,M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(sys.stdin.readline().strip()))
print(bfs())