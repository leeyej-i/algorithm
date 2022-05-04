# 백준 2234
# 골드 4 / 성곽

from collections import deque
import sys


def bfs1():
    global result1, result2
    visit = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                result1 += 1
                visit[i][j] = 1
                subResult = 0
                queue.append([i, j])
                while queue:
                    x, y = queue.popleft()
                    subResult += 1
                    for wall in range(4):
                        if data[x][y][wall] == '0':
                            xx = x + dx[wall]
                            yy = y + dy[wall]
                            if 0 <= xx < N and 0 <= yy < M and visit[xx][yy] == 0:
                                queue.append([xx, yy])
                                visit[xx][yy] = 1
            result2 = max(result2, subResult)


def count(i, j):
    global result3
    visit = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append([i, j])
    visit[i][j] = 1
    subResult = 0
    while queue:
        x, y = queue.popleft()
        subResult += 1
        for wall in range(4):
            if data[x][y][wall] == '0':
                xx = x + dx[wall]
                yy = y + dy[wall]
                if 0 <= xx < N and 0 <= yy < M and visit[xx][yy] == 0:
                    queue.append([xx, yy])
                    visit[xx][yy] = 1
    result3 = max(result3, subResult)


def brokeWall():
    for i in range(N):
        for j in range(M):
            if data[i][j][1] == '1' and j+1 < M:  # 동
                data[i][j][1] = '0'
                count(i, j)
                data[i][j][1] = '1'
            if data[i][j][0] == '1' and i+1 < N:  # 남
                data[i][j][0] = '0'
                count(i, j)
                data[i][j][0] = '1'


M, N = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        data[i][j] = list(bin(data[i][j])[2:].zfill(4))

# print(data)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result1, result2, result3 = 0, 0, 0
bfs1()
brokeWall()
print(result1)
print(result2)
print(result3)
