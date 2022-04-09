# 백준 17135
# 골드 4 / 캐슬 디펜스
from copy import deepcopy
from itertools import combinations
import sys


def killEnemy(i, j):
    ableKill = []
    for y in range(M):
        for x in range(N-1, -1, -1):
            if data[x][y] == 1:
                value = abs(i-x) + abs(j-y)
                if value <= D:
                    ableKill.append([value, y, x])
    if len(ableKill) == 0:
        return
    ableKill.sort()
    if [ableKill[0][2], ableKill[0][1]] in kill:
        return
    else:
        kill.append([ableKill[0][2], ableKill[0][1]])


def moveEnemy():
    check = 0
    for i in range(N-1, -1, -1):
        for j in range(M):
            if data[i][j] == 1:
                if i == N - 1:
                    data[i][j] = 0
                else:
                    data[i][j] = 0
                    data[i+1][j] = 1
                    check = 1
    return check


N, M, D = map(int, sys.stdin.readline().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

archer = []
for i in range(M):
    archer.append([N, i])

result = 0
for item in combinations(archer, 3):
    data = deepcopy(graph)
    sum = 0
    while True:
        kill = []
        for i, j in item:
            killEnemy(i, j)
        sum += len(kill)
        for i, j in kill:
            data[i][j] = 0

        if moveEnemy() == 0:
            break
    # print(item)
    # print(sum)
    result = max(result, sum)

print(result)
