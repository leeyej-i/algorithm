# 백준 14503
# 골드 4 / 로봇 청소기
from collections import deque
import sys

def bfs(startX, startY, dir):
    dx = [[0, 1, 0, -1], [-1, 0, 1, 0], [0, -1, 0, 1], [1, 0, -1, 0]]
    dy = [[-1, 0, 1, 0], [0, -1, 0, 1], [1, 0, -1, 0], [0, 1, 0, -1]]
    direction = dir
    queue = deque()
    queue.append([startX, startY])
    visit[startX][startY] = 1
    result = 1 #청소한 공간
    while queue :
        check = 0
        direction2 = direction
        x, y = queue.popleft()
        for i in range(4):
            direction2-=1
            if direction2 == -1 :
                direction2 = 3
            xx = x + dx[direction][i]
            yy = y + dy[direction][i]
            if 0<=xx<N and 0<=yy<M :
                if visit[xx][yy] == 0 and data[xx][yy] == 0:
                    visit[xx][yy] = visit[x][y] + 1
                    queue.append([xx,yy])
                    direction = direction2
                    result +=1
                    break
                else :
                    check+=1
        if check == 4 :
            xx = x + dx[direction][1]
            yy = y + dy[direction][1]
            if 0<=xx<N and 0<=yy<M and data[xx][yy] == 0 :
                queue.append([xx,yy])
            else :
                break
    
    return result
    
N, M = map(int,sys.stdin.readline().split())
r, c, d = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
visit = [[0 for _ in range(M)] for _ in range(N)]
print(bfs(r,c,d))
