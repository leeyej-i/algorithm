# 백준 2589
# 골드 5 / 보물섬
import sys
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visit = [[-1 for _ in range(M)] for _ in range(N)]
    visit[x][y] = 0
    time = 0
    while queue :
        pre_x, pre_y = queue.popleft()
        time = visit[pre_x][pre_y]
        for i in range(4):
            next_x = pre_x + dx[i]
            next_y = pre_y + dy[i]
            if 0<=next_x<N and 0<=next_y<M :
                if t_map[next_x][next_y] == 'L' and visit[next_x][next_y] == -1 :
                    queue.append([next_x, next_y])
                    visit[next_x][next_y] = time + 1
    # for item in visit:
    #     print(item)
    # print()
    return time
    

N, M = map(int,sys.stdin.readline().split())
t_map = []

# N*M 보물지도
for _ in range(N):
    t_map.append(list(sys.stdin.readline().strip()))


res = 0
for i in range(N):
    for j in range(M):
        if t_map[i][j] == 'L' :
            res = max(res, bfs(i,j))
            
print(res)