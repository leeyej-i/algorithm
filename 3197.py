# 백준 3197
# 플래 5 / 백조의 호수
from collections import deque
from copy import deepcopy
import sys


def bfs(melt):
    queue = deque(melt)
    queue2 = deque([[birds[0][0], birds[0][1]]])
    birdVisit[birds[0][0]][birds[0][1]] = 1
    time = 0
    while queue:
        while queue2:
            x, y = queue2.popleft()
            for k in range(4):
                xx = x + dx[k]
                yy = y + dy[k]
                if 0 <= xx < R and 0 <= yy < C and birdVisit[xx][yy] == 0:
                    if data[xx][yy] == '.':
                        queue2.append([xx, yy])
                        birdVisit[xx][yy] = 1
                    elif data[xx][yy] == 'L':
                        return time
                    else:
                        birdVisit[xx][yy] = 2

        for _ in range(len(queue)):
            x, y = queue.popleft()
            data[x][y] = '.'
            if birdVisit[x][y] == 2:
                queue2.append([x, y])
                birdVisit[x][y] = 1
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < R and 0 <= yy < C and meltVisit[xx][yy] == 0:
                    if data[xx][yy] == 'X':
                        queue.append([xx, yy])
                        meltVisit[xx][yy] = 1
        time += 1
    return time


R, C = map(int, sys.stdin.readline().split())
data = []
for _ in range(R):
    data.append(list(sys.stdin.readline().rstrip()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 물과 닿아있는 곳 melt에 저장
birds = []
visit = [[0 for _ in range(C)] for _ in range(R)]
melt = []
for i in range(R):
    for j in range(C):
        if data[i][j] == 'X' and visit[i][j] == 0:
            for k in range(4):
                ii = i + dx[k]
                jj = j + dy[k]
                if 0 <= ii < R and 0 <= jj < C:
                    if data[ii][jj] != 'X':
                        melt.append([i, j])
        elif data[i][j] == 'L':
            birds.append([i, j])


time = 0
meltVisit = [[0 for _ in range(C)] for _ in range(R)]
for item in melt:
    meltVisit[item[0]][item[1]] = 1
birdVisit = [[0 for _ in range(C)] for _ in range(R)]
time = bfs(melt)

print(time)
