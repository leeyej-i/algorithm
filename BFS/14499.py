# 백준 14499
# 골드 4 / 주사위 굴리기

import sys


def diceChange(dice, xx, yy):
    if data[xx][yy] == 0:
        data[xx][yy] = dice[3]
    else:
        dice[3] = data[xx][yy]
        data[xx][yy] = 0


def moveDice(x, y):
    # 세로 가로(| -)
    dice = [0, 0, 0, 0, 0, 0]
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]

    for order in orders:
        xx = x + dx[order]
        yy = y + dy[order]
        if 0 <= xx < N and 0 <= yy < M:
            if order == 1:  # 동쪽
                dice[4], dice[5] = dice[5], dice[4]
                dice[4], dice[3] = dice[3], dice[4]
                dice[5], dice[1] = dice[1], dice[5]
            elif order == 2:  # 서쪽
                dice[4], dice[5] = dice[5], dice[4]
                dice[4], dice[1] = dice[1], dice[4]
                dice[5], dice[3] = dice[3], dice[5]
            elif order == 3:  # 북쪽
                dice[0], dice[1] = dice[1], dice[0]
                dice[1], dice[2] = dice[2], dice[1]
                dice[2], dice[3] = dice[3], dice[2]
            else:  # 남쪽
                dice[0], dice[1] = dice[1], dice[0]
                dice[2], dice[3] = dice[3], dice[2]
                dice[0], dice[2] = dice[2], dice[0]

            diceChange(dice, xx, yy)
            # print(dice)
            print(dice[1])
            x, y = xx, yy
        else:
            continue


N, M, x, y, K = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

orders = list(map(int, sys.stdin.readline().split()))

moveDice(x, y)
