# 백준 15683
# 골드 4 / 감시
from copy import deepcopy
import sys


def up(item, x, y):
    while True:
        xx = x + dx[0]
        yy = y + dy[0]
        if 0 <= xx < N and 0 <= yy < M and item[xx][yy] != 6:
            if item[xx][yy] == 0:
                item[xx][yy] = -1
                x, y = xx, yy
            else:
                x, y = xx, yy
                continue
        else:
            break
    return item


def right(item, x, y):
    while True:
        xx = x + dx[1]
        yy = y + dy[1]
        if 0 <= xx < N and 0 <= yy < M and item[xx][yy] != 6:
            if item[xx][yy] == 0:
                item[xx][yy] = -1
                x, y = xx, yy
            else:
                x, y = xx, yy
                continue
        else:
            break
    return item


def left(item, x, y):
    while True:
        xx = x + dx[3]
        yy = y + dy[3]
        if 0 <= xx < N and 0 <= yy < M and item[xx][yy] != 6:
            if item[xx][yy] == 0:
                item[xx][yy] = -1
                x, y = xx, yy
            else:
                x, y = xx, yy
                continue
        else:
            break
    return item


def down(item, x, y):
    while True:
        xx = x + dx[2]
        yy = y + dy[2]
        if 0 <= xx < N and 0 <= yy < M and item[xx][yy] != 6:
            if item[xx][yy] == 0:
                item[xx][yy] = -1
                x, y = xx, yy
            else:
                x, y = xx, yy
                continue
        else:
            break
    return item


def cctv1(datas, x, y):
    dataArray = []
    for item in datas:
        copyItem = deepcopy(item)
        dataArray.append(up(copyItem, x, y))
        copyItem = deepcopy(item)
        dataArray.append(right(copyItem, x, y))
        copyItem = deepcopy(item)
        dataArray.append(left(copyItem, x, y))
        copyItem = deepcopy(item)
        dataArray.append(down(copyItem, x, y))
    return dataArray


def cctv2(datas, x, y):
    dataArray = []
    for item in datas:
        copyItem = deepcopy(item)
        dataArray.append(up(down(copyItem, x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(right(left(copyItem, x, y), x, y))
    return dataArray


def cctv3(datas, x, y):
    dataArray = []
    for item in datas:
        copyItem = deepcopy(item)
        dataArray.append(up(right(copyItem, x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(right(down(copyItem, x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(down(left(copyItem, x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(left(up(copyItem, x, y), x, y))
    return dataArray


def cctv4(datas, x, y):
    dataArray = []
    for item in datas:
        copyItem = deepcopy(item)
        dataArray.append(up(right(left(copyItem, x, y), x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(up(right(down(copyItem, x, y), x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(down(right(left(copyItem, x, y), x, y), x, y))
        copyItem = deepcopy(item)
        dataArray.append(up(down(left(copyItem, x, y), x, y), x, y))
    return dataArray


def cctv5(datas, x, y):
    dataArray = []
    for item in datas:
        copyItem = deepcopy(item)
        dataArray.append(
            down(up(right(left(copyItem, x, y), x, y), x, y), x, y))
    return dataArray


def checkArea(item):
    num = 0
    for i in range(N):
        for j in range(M):
            if item[i][j] == 0:
                num += 1
    return num


def cctvOperate(data, cctvs):
    datas = [data]
    while cctvs:
        cctvNum, x, y = cctvs.pop()
        if cctvNum == 1:
            datas = cctv1(datas, x, y)
        elif cctvNum == 2:
            datas = cctv2(datas, x, y)
        elif cctvNum == 3:
            datas = cctv3(datas, x, y)
        elif cctvNum == 4:
            datas = cctv4(datas, x, y)
        elif cctvNum == 5:
            datas = cctv5(datas, x, y)

    res = N*M
    for item in datas:
        res = min(res, checkArea(item))

    return res


N, M = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))


cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= data[i][j] <= 5:
            cctvs.append([data[i][j], i, j])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(cctvOperate(data, cctvs))
