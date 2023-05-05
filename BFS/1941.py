# 백준 1941
# 골드 3 / 소문난 7공주
from collections import deque
import sys


def isConnect(cnt):
    visit2 = [[0 for _ in range(5)] for _ in range(5)]
    x, y = cnt // 5, cnt % 5
    queue = deque()
    queue.append([x, y])
    visit2[x][y] = 1
    subResult = 0
    while queue:
        xx, yy = queue.popleft()
        subResult += 1
        for i in range(4):
            xxx = xx + dx[i]
            yyy = yy + dy[i]
            if 0 <= xxx < 5 and 0 <= yyy < 5 and visit2[xxx][yyy] == 0:
                if visit[xxx][yyy] == 1:
                    visit2[xxx][yyy] = 1
                    queue.append([xxx, yyy])
    if subResult == 7:
        return 1
    else:
        return 0


def backTracking(cnt, total, yTeam):
    global result
    if yTeam >= 4:
        return

    elif total == 7:
        if isConnect(cnt - 1) == 1:
            # for item in visit:
            #     print(item)
            # print()
            result += 1
        return

    for x in range(cnt, 25):
        i, j = x // 5, x % 5
        if data[i][j] == 'Y':
            visit[i][j] = 1
            backTracking(x+1, total+1, yTeam+1)
            visit[i][j] = 0
        else:
            visit[i][j] = 1
            backTracking(x+1, total+1, yTeam)
            visit[i][j] = 0


data = []
for _ in range(5):
    data.append(list(sys.stdin.readline().strip()))

result = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visit = [[0 for _ in range(5)] for _ in range(5)]
backTracking(0, 0, 0)
print(result)
