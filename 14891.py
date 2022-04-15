# 백준 14891
# 골드 5 / 톱니바퀴
from collections import deque
import sys


def gearRotate():
    dx = [1, -1]
    for gearNum, vector in rotate:
        moveGear = []
        visit = [0 for _ in range(5)]
        moveGear.append([gearNum, vector])
        visit[gearNum] = 1
        for i in range(2):
            newGearNum = gearNum + dx[i]
            if 1 <= newGearNum <= 4 and visit[newGearNum] == 0:
                if i == 0 and gears[gearNum][2] != gears[newGearNum][6]:
                    moveGear.append([newGearNum, (-1)*vector])
                    visit[newGearNum] = 1
                if i == 1 and gears[gearNum][6] != gears[newGearNum][2]:
                    moveGear.append([newGearNum, (-1)*vector])
                    visit[newGearNum] = 1
        check = 1
        for j in range(check, len(moveGear)):
            currentGearNum, currentVector = moveGear[j][0], moveGear[j][1]
            for i in range(2):
                nextGearNum = currentGearNum + dx[i]
                if 1 <= nextGearNum <= 4 and visit[nextGearNum] == 0:
                    if i == 0 and gears[currentGearNum][2] != gears[nextGearNum][6]:
                        moveGear.append([nextGearNum, (-1)*currentVector])
                        visit[nextGearNum] = 1
                    if i == 1 and gears[currentGearNum][6] != gears[nextGearNum][2]:
                        moveGear.append([nextGearNum, (-1)*currentVector])
                        visit[nextGearNum] = 1
            check = j

        for j in range(check, len(moveGear)):
            currentGearNum, currentVector = moveGear[j][0], moveGear[j][1]
            for i in range(2):
                nextGearNum = currentGearNum + dx[i]
                if 1 <= nextGearNum <= 4 and visit[nextGearNum] == 0:
                    if i == 0 and gears[currentGearNum][2] != gears[nextGearNum][6]:
                        moveGear.append([nextGearNum, (-1)*currentVector])
                        visit[nextGearNum] = 1
                    if i == 1 and gears[currentGearNum][6] != gears[nextGearNum][2]:
                        moveGear.append([nextGearNum, (-1)*currentVector])
                        visit[nextGearNum] = 1

        for moveNum, moveVector in moveGear:
            if moveVector == 1:
                gears[moveNum].appendleft(gears[moveNum].pop())
            elif moveVector == -1:
                gears[moveNum].append(gears[moveNum].popleft())


# 12시 = 0 / 3시 = 2 / 6시 = 4 / 9시 = 6
gears = [deque()]
gears.append(deque(sys.stdin.readline().strip()))
gears.append(deque(sys.stdin.readline().strip()))
gears.append(deque(sys.stdin.readline().strip()))
gears.append(deque(sys.stdin.readline().strip()))

K = int(sys.stdin.readline().strip())
# 1 = 시계 방향
rotate = []
for _ in range(K):
    rotate.append(list(map(int, sys.stdin.readline().split())))


gearRotate()
result = 0
for i in range(1, 5):
    if gears[i][0] == '1':
        result += 2**(i-1)

print(result)
