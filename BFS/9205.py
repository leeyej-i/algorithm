# 백준 9205
# 실버 1 / 맥주 마시면서 걸어가기
from collections import deque
import sys

def bfs():
    queue = deque()
    queue.append([homeX,homeY])
    while queue :
        x, y = queue.popleft()
        if abs(festivalX - x) + abs(festivalY - y) <= 1000 :
            return 1
        for i in range(n):
            if visit[i] == 0 :
                distance = abs(stores[i][0] - x) + abs(stores[i][1] - y)
                if distance <= 1000 :
                    queue.append([stores[i][0], stores[i][1]])
                    visit[i] = 1
    return 0
                
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    homeX, homeY = map(int,sys.stdin.readline().split())
    stores = []
    for _ in range(n) :
        stores.append(list(map(int,sys.stdin.readline().split())))
    festivalX, festivalY = map(int,sys.stdin.readline().split())

    visit = [0 for _ in range(n)]
    if bfs() :
        print("happy")
    else :
        print("sad")
        