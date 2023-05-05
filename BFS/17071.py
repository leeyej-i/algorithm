# 백준 12851
# 골드 1 / 숨바꼭질 5
from collections import deque
import sys


def bfs():
    global K
    queue = deque()
    queue.append(N)
    result = 0
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == K:
                return result
            for xx in (x+1, x-1, x*2):
                if 0 <= xx <= 500000:
                    if visit[xx] == 0:
                        visit[xx] = result
                        queue.append(xx)
                    elif visit[xx] > result:
                        queue.append(xx)
                        visit[xx] = result
        result += 1
        K += result
        if K > 500000:
            return -1


N, K = map(int, sys.stdin.readline().split())
visit = [0 for _ in range(500001)]
res = bfs()
print(res)
