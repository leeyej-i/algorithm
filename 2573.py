# 백준 2573
# 골드 4 / 빙산
from collections import deque
import sys

def bfs():
    year = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while True:
        visit = [[-1 for _ in range(M)]for _ in range(N)]
        iceCheck = 0 #빙하 덩어리 개수 체크
        zeroCheck = 0 #빙하가 다 녹아버린 경우 체크
        for i in range(N):
            for j in range(M):
                if data[i][j] != 0 and visit[i][j] == -1:
                    zeroCheck+=1
                    queue = deque()
                    queue.append([i, j])
                    visit[i][j] = 0
                    while queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            xx = x+dx[k]
                            yy = y+dy[k]
                            if 0 <= xx < N and 0 <= yy < M and visit[xx][yy] == -1:
                                if data[xx][yy] != 0:
                                    queue.append([xx, yy])
                                    visit[xx][yy] = 0
                                else:
                                    visit[x][y] += 1
                    iceCheck += 1
                    if iceCheck >= 2:
                        return year
        if zeroCheck== 0 :
            return 0
        year +=1
        for i in range(N):
            for j in range(M):
                if visit[i][j] != -1 :
                    if visit[i][j] >= data[i][j]:
                        data[i][j] = 0
                    else :
                        data[i][j] = data[i][j] - visit[i][j]
        

N, M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
print(bfs())