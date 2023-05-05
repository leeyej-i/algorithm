# 백준 1743
# 실버 1 / 음식물 피하기
import sys
from collections import deque

def bfs(i,j):
    queue= deque()
    queue.append([i,j])
    visit[i][j] = 1
    cnt = 1
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while queue :
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<N and 0<=yy<M :
                if space[xx][yy] == 1 and visit[xx][yy] == 0 :
                    visit[xx][yy] = 1
                    queue.append([xx,yy])
                    cnt += 1
    return cnt

N, M, K = map(int,sys.stdin.readline().split())

space = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    r, c = r-1, c-1
    space[r][c] = 1

# print(space)
visit = [[0 for _ in range(M)] for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if space[i][j] == 1 and visit[i][j] == 0:
            res = max(bfs(i,j), res)

print(res)