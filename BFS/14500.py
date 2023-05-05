# 백준 14500
# 골드 5 / 테트로미노
from collections import deque
import sys


def bfs(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([i, j, 1, data[i][j], -1, -1])
    maxSum = 0
    while queue:
        x, y, num, sum, prevX, prevY = queue.popleft()
        if num == 4:
            maxSum = max(maxSum, sum)
            continue
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M:
                if xx != prevX or yy != prevY:
                    queue.append([xx, yy, num+1, sum + data[xx][yy], x, y])
    return maxSum


def mountain(i, j):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    plus = []
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < N and 0 <= y < M:
            plus.append(data[x][y])
    if len(plus) == 4:
        return data[i][j] + sum(plus) - min(plus)
    elif len(plus) == 3:
        return data[i][j] + sum(plus)
    else:
        return 0


N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, bfs(i, j), mountain(i, j))

print(result)
