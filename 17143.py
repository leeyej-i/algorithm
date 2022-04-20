# 백준 17143
# 골드 2 / 낚시왕

from collections import deque
import sys


def huntShark(y):
    global result
    for i in range(R):
        if len(data[i][y]) > 0:
            s, d, z = data[i][y].popleft()
            result += z
            return


def moveShark():
    visit = [[0 for _ in range(C)] for _ in range(R)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(R):
        for j in range(C):
            if (len(data[i][j]) > visit[i][j]):
                s, d, z = data[i][j].popleft()
                dxx, dyy = dx[d], dy[d]
                ii, jj = i, j
                for _ in range(s):
                    if (ii == R-1 and dxx == 1) or (ii == 0 and dxx == -1):
                        dxx = -1 * dxx
                    if (jj == C-1 and dyy == 1) or (jj == 0 and dyy == -1):
                        dyy = -1 * dyy
                    ii = ii + dxx
                    jj = jj + dyy
                if dxx == -1 and dyy == 0:
                    d = 0
                elif dxx == 1 and dyy == 0:
                    d = 1
                elif dyy == -1 and dxx == 0:
                    d = 3
                else:
                    d = 2
                data[ii][jj].append([s, d, z])
                visit[ii][jj] += 1


# R*C / M = 상어의 수
R, C, M = map(int, sys.stdin.readline().split())
data = [[deque() for _ in range(C)] for _ in range(R)]

manDic = -1
for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    r, c, d = r-1, c-1, d-1
    # s 속력 / d 방향(1 = 위 / 2 = 아래 / 3 = 오른쪽 / 4 = 왼쪽) / z 크기
    data[r][c].append([s, d, z])

result = 0
while True:
    manDic += 1
    if manDic == C:
        break
    huntShark(manDic)
    moveShark()
    for i in range(R):
        for j in range(C):
            if len(data[i][j]) >= 2:
                maxS, maxD, maxZ = 0, 0, 0
                while data[i][j]:
                    s, d, z = data[i][j].popleft()
                    if z > maxZ:
                        maxS, maxD, maxZ = s, d, z
                data[i][j].append([maxS, maxD, maxZ])


print(result)
