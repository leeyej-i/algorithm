# 백준 17406
# 골드 4 / 배열 돌리기 4
from copy import deepcopy
from itertools import permutations
import sys


def rotate(order, copyData):
    for i in range(len(order)):
        od = order[i]
        start = [od[0] - od[2]-1, od[1]-od[2]-1]
        end = [od[0] + od[2]-1, od[1] + od[2]-1]

        for j in range(od[2]*2, 1, -2):
            startData = copyData[start[0]][start[1]]
            for k in range(start[0], end[0]):
                copyData[k][start[1]] = copyData[k+1][start[1]]

            for k in range(start[1], end[1], 1):
                copyData[end[0]][k] = copyData[end[0]][k+1]

            for k in range(end[0], start[0], -1):
                copyData[k][end[1]] = copyData[k-1][end[1]]

            for k in range(end[1], start[1] + 1, -1):
                copyData[start[0]][k] = copyData[start[0]][k-1]

            copyData[start[0]][start[1]+1] = startData
            start[0], start[1] = start[0] + 1, start[1]+1
            end[0], end[1] = end[0] - 1, end[1] - 1


# N*M  / K = 회전 연산 수
N, M, K = map(int, sys.stdin.readline().split())

datas = []
for _ in range(N):
    datas.append(list(map(int, sys.stdin.readline().split())))

orders = []
for _ in range(K):
    orders.append(list(map(int, sys.stdin.readline().split())))

result = 5000
for order in permutations(orders, len(orders)):
    copyDatas = deepcopy(datas)
    rotate(order, copyDatas)

    for data in copyDatas:
        result = min(result, sum(data))


print(result)
