# 백준 16234
# 골드 5 / 인구이동
from collections import deque
import sys


def makeUnion():
    check = 0
    for i in range(N):
        for j in range(N):
            if i != 0 and L <= abs(population[i][j] - population[i-1][j]) <= R:
                union[i][j][0] = 1
                check = 1
            if j != N-1 and L <= abs(population[i][j] - population[i][j+1]) <= R:
                union[i][j][1] = 1
                check = 1
            if i != N-1 and L <= abs(population[i][j] - population[i+1][j]) <= R:
                union[i][j][2] = 1
                check = 1
            if j != 0 and L <= abs(population[i][j] - population[i][j-1]) <= R:
                union[i][j][3] = 1
                check = 1
    return check


def bfs(i, j):
    # 북동남서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    queue = deque()
    queue.append([i, j])
    visit[i][j] = 1
    sum = population[i][j]
    unionList = [[i, j]]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if union[x][y][i] == 1:
                xx = x + dx[i]
                yy = y + dy[i]
                if 0 <= xx < N and 0 <= yy < N and visit[xx][yy] == 0:
                    visit[xx][yy] = 1
                    queue.append([xx, yy])
                    sum += population[xx][yy]
                    unionList.append([xx, yy])
    if len(unionList) == 1:
        return
    else:
        value = sum // len(unionList)
        for a, b in unionList:
            population[a][b] = value


N, L, R = map(int, sys.stdin.readline().split())
population = []
for _ in range(N):
    population.append(list(map(int, sys.stdin.readline().split())))

result = 0
while True:
    # 국경선(북 -> 동 -> 남 -> 서)
    union = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]
    unionNum = makeUnion()
    if unionNum == 0:
        break
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                bfs(i, j)
    result += 1
print(result)
