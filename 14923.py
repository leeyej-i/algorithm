# 백준 14923
# 골드 4 / 미로 탈출

import sys
from collections import deque

def bfs(sx, sy, fx, fy) :
    # 현재 위치 좌표, 움직인 거리, 벽 부순 유무
    queue = deque([[sx, sy, 0, 0]])
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    # 현재 위치 visit표시
    data[sx][sy] = 2
    while queue : 
        x, y, distance, check = queue.popleft()
        if x == fx and y == fy :
            return distance
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<N and 0<=yy<M : 
                # 벽 부시기 가능
                if check == 0 :
                    # 벽 안부셔도 되는 경우
                    if data[xx][yy] == 0 :
                        queue.append([xx,yy,distance+1, check])
                        data[xx][yy] = 2
                    # 벽을 부셔야 하는 경우
                    if data[xx][yy] == 1 :
                        queue.append([xx,yy,distance+1, 1])
                    if data[xx][yy] == 3 :
                        queue.append([xx,yy,distance+1, check])
                        data[xx][yy] = 2
                else :
                    if data[xx][yy] == 0 :
                        queue.append([xx,yy,distance+1,check])
                        data[xx][yy] = 3
    return -1
    
    
N, M = map(int,sys.stdin.readline().split())

# E => 현재위치, E => 도착위치
Hx, Hy = map(int, sys.stdin.readline().split())
Ex, Ey = map(int, sys.stdin.readline().split())

# 0부터 시작하게 좌표 수정
Hx, Hy = Hx - 1 , Hy - 1 
Ex, Ey = Ex - 1, Ey - 1

data = []
for _ in range(N) :
    data.append(list(map(int,sys.stdin.readline().split())))

res = bfs(Hx, Hy, Ex, Ey)
print(res)