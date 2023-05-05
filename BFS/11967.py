# 백준 11967
# 골드 2 / 불켜기
from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

rooms = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x, y, a, b = map(int, sys.stdin.readline().split())
    rooms[x][y].append([a, b])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

light = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 불켜진방
visit = [[0 for _ in range(N+1)] for _ in range(N+1)]  # 방문리스트

queue = deque()
light[1][1] = visit[1][1] = 1
res = 1
queue.append([1, 1])
while(queue):
    cur_x, cur_y = queue.popleft()  # 현재위치
    for next_x, next_y in rooms[cur_x][cur_y]:
        if light[next_x][next_y] == 0:  # 꺼져있는 경우 다 켜기
            light[next_x][next_y] = 1
            res += 1
            for i in range(4):  # 킨 곳이 갈 수 있으면 queue에 넣기
                check_x = next_x + dx[i]
                check_y = next_y + dy[i]
                if 0 < check_x < N+1 and 0 < check_y < N+1:
                    if visit[check_x][check_y] == 1:
                        queue.append([next_x, next_y])
                        visit[next_x][next_y] = 1
    for i in range(4):  # 주변 탐색해서 불켜졌는데 방문한적이 없으면
        check_x = cur_x + dx[i]
        check_y = cur_y + dy[i]
        if 0 < check_x < N+1 and 0 < check_y < N+1:
            if visit[check_x][check_y] == 0 and light[check_x][check_y] == 1:
                queue.append([check_x, check_y])
                visit[check_x][check_y] = 1


print(res)
