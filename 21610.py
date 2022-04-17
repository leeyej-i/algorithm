# 백준 21610
# 골드 5 / 마법사 상어와 비바라기

import sys


def cloudOrder(vector, value):
    moveCloud = [[0 for _ in range(N)] for _ in range(N)]
    for x, y in cloud:
        xx, yy = x, y
        for _ in range(value):
            xx = xx + dx[vector]
            yy = yy + dy[vector]
            if xx < 0:
                xx = N-1
            if xx >= N:
                xx = 0
            if yy < 0:
                yy = N-1
            if yy >= N:
                yy = 0

        data[xx][yy] += 1
        moveCloud[xx][yy] = 1

    for xx in range(N):
        for yy in range(N):
            if moveCloud[xx][yy] == 1:
                check = 0
                for i in range(1, 9):
                    if abs(dx[i]) + abs(dy[i]) == 2:
                        xxx = xx + dx[i]
                        yyy = yy + dy[i]
                        if 0 <= xxx < N and 0 <= yyy < N and data[xxx][yyy] > 0:
                            check += 1
                data[xx][yy] += check

    nextCloud = []
    for i in range(N):
        for j in range(N):
            if data[i][j] >= 2:
                if moveCloud[i][j] != 1:
                    nextCloud.append([i, j])
                    data[i][j] -= 2

    return nextCloud


N, M = map(int, sys.stdin.readline().split())

# N*N
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

# 이동정보
move = []
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split())
    move.append([d, s])

# 1부터 순서대로
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cloud = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for vector, value in move:
    cloud = cloudOrder(vector, value)

result = 0
for i in data:
    result += sum(i)

print(result)
