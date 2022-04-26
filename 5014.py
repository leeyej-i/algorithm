# 백준 5014
# 골드 5 / 스타트링크
from collections import deque
import sys


def bfs(start, end, up, down):
    queue = deque()
    dx = [up, (-1)*down]
    queue.append(start)
    visit[start] = 1
    res = 0
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            if x == end:
                return res
            for i in range(2):
                xx = x + dx[i]
                if 1 <= xx <= F and visit[xx] == 0:
                    queue.append(xx)
                    visit[xx] = 1
        res += 1
    return -1


# F = 전체 층 / S -> G
F, S, G, U, D = map(int, sys.stdin.readline().split())
visit = [0 for _ in range(F+1)]
result = bfs(S, G, U, D)
if result == -1:
    print("use the stairs")
else:
    print(result)
