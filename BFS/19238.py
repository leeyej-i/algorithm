# 백준 19238
# 골드 3 / 스타트 택시

from collections import deque
import sys


def bfs(fuel, taxiX, taxiY):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    queue.append([taxiX, taxiY, 0])
    visit[taxiX][taxiY] = -1
    if data[taxiX][taxiY] == 0:
        check = 0
        while queue:
            for _ in range(len(queue)):
                x, y, distance = queue.popleft()
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if 0 <= xx < N and 0 <= yy < N and visit[xx][yy] == 0:
                        if data[xx][yy] >= 2:
                            check = 1
                            visit[xx][yy] = distance + 1
                        if data[xx][yy] == 0:
                            queue.append([xx, yy, distance + 1])
                            visit[xx][yy] = -1
            if check != 0:
                break
        if check == 0:
            return 0, xx, yy

        check2 = 0
        for i in range(N):
            for j in range(N):
                if visit[i][j] != 0 and visit[i][j] != -1 and check2 == 0:
                    if fuel > visit[i][j]:
                        fuel -= visit[i][j]
                        taxiX, taxiY = i, j
                        check2 = 1
                        break
                    else:
                        return 0, i, j

    queue2 = deque()
    queue2.append([taxiX, taxiY, 0])
    visit2 = [[0 for _ in range(N)] for _ in range(N)]
    visit2[taxiX][taxiY] = 1
    while queue2:
        x, y, distance = queue2.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N and visit2[xx][yy] == 0 and data[xx][yy] != 1:
                if xx == passengers[taxiX][taxiY][0] and yy == passengers[taxiX][taxiY][1]:
                    data[taxiX][taxiY] = 0
                    visit2[xx][yy] = 1
                    if fuel >= distance + 1:
                        fuel -= (distance + 1)
                        fuel += (distance+1) * 2
                        return fuel, xx, yy
                    else:
                        return 0, xx, yy
                else:
                    queue2.append([xx, yy, distance+1])
                    visit2[xx][yy] = 1
    return 0, xx, yy


# N*N / M = 승객 수 / 연료
N, M, fuel = map(int, sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

taxiLocX, taxiLocY = map(int, sys.stdin.readline().split())
taxiLocX, taxiLocY = taxiLocX - 1, taxiLocY - 1

passengers = [[[] for _ in range(N)] for _ in range(N)]
for i in range(2, M+2):
    startX, startY, finishX, finishY = map(int, sys.stdin.readline().split())
    data[startX-1][startY-1] = i
    passengers[startX-1][startY-1].append(finishX - 1)
    passengers[startX-1][startY-1].append(finishY - 1)

res = fuel
for _ in range(M):
    res, taxiLocX, taxiLocY = bfs(res, taxiLocX, taxiLocY)
    if res == 0:
        res = -1
        break

print(res)
