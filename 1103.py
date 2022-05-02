# 백준 1103
# 골드 2 / 게임
import sys


def dfs(x, y, res):
    global result
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        xx = x + dx[i]*int(data[x][y])
        yy = y + dy[i]*int(data[x][y])
        if 0 <= xx < N and 0 <= yy < M and data[xx][yy] != 'H':
            if visit[xx][yy] == 1:
                print(-1)
                exit()
            if visit2[xx][yy] >= res + 1:
                continue
            visit[xx][yy] = 1
            dfs(xx, yy, res+1)
            visit[xx][yy] = 0
    visit2[x][y] = res
    result = max(result, res)


N, M = map(int, sys.stdin.readline().split())

data = []
for _ in range(N):
    data.append(list(sys.stdin.readline().rstrip()))
result = 0
visit = [[0 for _ in range(M)]for _ in range(N)]
visit2 = [[0 for _ in range(M)]for _ in range(N)]
visit2[0][0] = 1
dfs(0, 0, 1)
print(result)
