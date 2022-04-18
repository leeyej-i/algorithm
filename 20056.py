# 백준 20056
# 골드 4 / 마법사 상어와 파이어볼

import sys


def moveFireBall():
    fireBall = []
    fireBallInfo = []
    for x in range(N):
        for y in range(N):
            for _ in range(len(data[x][y])):
                m, s, d = data[x][y].pop()
                xx, yy = x, y
                for _ in range(s):
                    xx = xx + dx[d]
                    yy = yy + dy[d]
                    if xx < 0:
                        xx = N-1
                    if yy < 0:
                        yy = N-1
                    if xx >= N:
                        xx = 0
                    if yy >= N:
                        yy = 0
                fireBallInfo.append([m, s, d])
                fireBall.append([xx, yy])

    for i in range(len(fireBall)):
        data[fireBall[i][0]][fireBall[i][1]].append(fireBallInfo[i])
    return fireBall


def sepDiv(fireBall):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    twoFireBall = []
    for x, y in fireBall:
        if visit[x][y] == 0:
            visit[x][y] += 1
        elif visit[x][y] == 1:
            twoFireBall.append([x, y])
            visit[x][y] += 1
        else:
            visit[x][y] += 1

    for x, y in twoFireBall:
        mSum, sSum = 0, 0
        dArray = []
        for _ in range(len(data[x][y])):
            m, s, d = data[x][y].pop()
            mSum += m
            sSum += s
            dArray.append(d)

        check1, check2 = 0, 0
        for item in dArray:
            if item % 2 == 0:
                check1 += 1
            else:
                check2 += 1

        nextM = mSum // 5
        if nextM == 0:
            continue
        nextS = sSum // visit[x][y]
        if check1 * check2 == 0:

            data[x][y].append([nextM, nextS, 0])
            data[x][y].append([nextM, nextS, 2])
            data[x][y].append([nextM, nextS, 4])
            data[x][y].append([nextM, nextS, 6])
        else:
            data[x][y].append([nextM, nextS, 1])
            data[x][y].append([nextM, nextS, 3])
            data[x][y].append([nextM, nextS, 5])
            data[x][y].append([nextM, nextS, 7])


# N*N / M = 파이어볼 개수 / K = 명령횟수
N, M, K = map(int, sys.stdin.readline().split())


data = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    # 위치(r,c) / m = 질량 / s = 속력 / d = 방향
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    data[r-1][c-1].append([m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    fireBall = moveFireBall()  # 이동
    sepDiv(fireBall)  # 합체 & 분리

result = 0
for i in range(N):
    for j in range(N):
        for k in range(len(data[i][j])):
            result += data[i][j][k][0]

print(result)
