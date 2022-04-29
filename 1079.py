# 백준 1079
# 골드 2 / 마피아
from copy import deepcopy
import sys


def increase(i):
    for j in range(N):
        people[j] += rList[i][j]


def decrease(i):
    for j in range(N):
        people[j] -= rList[i][j]


def backTracking(mafiaNum, day, total):
    global result
    if visit[mafiaNum] == 1 or total == 1:
        result = max(result, day)
        return

    # 밤
    if total % 2 == 0:
        for i in range(N):
            if i != mafiaNum and visit[i] == 0:
                visit[i] = 1
                increase(i)
                backTracking(mafiaNum, day+1, total-1)
                visit[i] = 0
                decrease(i)
    else:  # 낮
        subResult = -1
        killNum = -1
        for i in range(N):
            if visit[i] == 0:
                if subResult < people[i]:
                    subResult = people[i]
                    killNum = i
        visit[killNum] = 1
        backTracking(mafiaNum, day, total-1)
        visit[killNum] = 0


N = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
rList = []
for _ in range(N):
    rList.append(list(map(int, sys.stdin.readline().split())))

num = int(sys.stdin.readline())

visit = [0 for _ in range(N)]
result = 0
backTracking(num, 0, N)
print(result)
