# 백준 16928
# 실버 1 / 뱀과 사다리 게임
from collections import deque
import sys

def bfs():
    dx = [1,2,3,4,5,6]
    queue = deque()
    queue.append([1,0])
    while queue :
        x, temp = queue.popleft()
        if x == 100 :
            return temp
        for i in range(6):
            xx = x + dx[i]
            if xx <= 100 and visit[xx]==0:
                if ladder_snake[xx] != 0:
                    visit[xx]=1
                    xx = ladder_snake[xx]
                visit[xx] = 1
                queue.append([xx, temp+1])

N,M = map(int,sys.stdin.readline().split())
ladder_snake = [0 for i in range(101)]
visit = [0 for i in range(101)]
for _ in range(N+M) :
    x,y = map(int,sys.stdin.readline().split())
    ladder_snake[x] = y

print(bfs())