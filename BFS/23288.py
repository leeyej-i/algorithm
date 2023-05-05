# 백준 23288
# 골드 3 / 주사위 굴리기 2
from collections import deque
import sys


def bfs(i, j):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append([i, j])
    visit = [[0 for _ in range(M)]for _ in range(N)]
    visit[i][j] = 1
    result = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx < N and 0 <= yy < M and visit[xx][yy] == 0:
                if data[xx][yy] == data[x][y]:
                    queue.append([xx, yy])
                    result += 1
                    visit[xx][yy] = 1
    return result


def diceCheck(num):
    if num == 0:  # 동쪽
        dice[1], dice[5] = dice[5], dice[1]
        dice[0], dice[1] = dice[1], dice[0]
        dice[1], dice[3] = dice[3], dice[1]
    if num == 1:  # 남쪽
        dice[5], dice[4] = dice[4], dice[5]
        dice[4], dice[3] = dice[3], dice[4]
        dice[3], dice[2] = dice[2], dice[3]
    if num == 2:  # 서쪽
        dice[0], dice[5] = dice[5], dice[0]
        dice[0], dice[1] = dice[1], dice[0]
        dice[0], dice[3] = dice[3], dice[0]
    if num == 3:  # 북쪽
        dice[5], dice[2] = dice[2], dice[5]
        dice[4], dice[3] = dice[3], dice[4]
        dice[4], dice[2] = dice[2], dice[4]


N, M, K = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

dice = [4, 3, 2, 1, 5, 6]
currentDice = dice[5]
currentLoc = [0, 0]
# 동 남 서 북(시계방향)
vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 0 = 동 / 1 = 남 / 2 = 서 / 3 = 북
currentVector = 0
sum = 0
for _ in range(K):
    currentLoc[0] += vector[currentVector][0]
    currentLoc[1] += vector[currentVector][1]
    if currentLoc[0] == -1 or currentLoc[0] == N or currentLoc[1] == -1 or currentLoc[1] == M:
        currentLoc[0] -= vector[currentVector][0]
        currentLoc[1] -= vector[currentVector][1]
        currentVector = (currentVector + 2) % 4
        currentLoc[0] += vector[currentVector][0]
        currentLoc[1] += vector[currentVector][1]
    diceCheck(currentVector)
    currentDice = dice[5]
    score = bfs(currentLoc[0], currentLoc[1]) * \
        data[currentLoc[0]][currentLoc[1]]
    sum += score
    if currentDice > data[currentLoc[0]][currentLoc[1]]:
        currentVector += 1
    elif currentDice < data[currentLoc[0]][currentLoc[1]]:
        currentVector -= 1

    if currentVector == 4:
        currentVector = 0
    elif currentVector == -1:
        currentVector = 3

print(sum)
