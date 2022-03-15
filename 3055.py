# 백준 3055
# 골드 4 / 탈출
from collections import deque
import sys

def func():
    dochi_queue = deque()
    water_queue = deque()
    for i in range(R):
        for j in range(C):
            if data[i][j] == '*':
                water_queue.append([i,j])
            if data[i][j] == 'S':
                dochi_queue.append([i,j])
    time = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while dochi_queue :
        time +=1
        water_len = len(water_queue)
        while water_len :
            water_x, water_y= water_queue.popleft()
            for k in range(4):
                water_xx = water_x + dx[k]
                water_yy = water_y + dy[k]
                if 0<=water_xx<R and 0<=water_yy<C:
                    if data[water_xx][water_yy] == '.' or data[water_xx][water_yy] == 'S':
                        data[water_xx][water_yy] = '*'
                        water_queue.append([water_xx, water_yy])
            water_len-=1
        dochi_len = len(dochi_queue)
        while dochi_len :
            dochi_x, dochi_y= dochi_queue.popleft()
            for l in range(4):
                dochi_xx = dochi_x + dx[l]
                dochi_yy = dochi_y + dy[l]
                if 0<=dochi_xx<R and 0<=dochi_yy<C:
                    if data[dochi_xx][dochi_yy] == 'D':
                        return time
                    if data[dochi_xx][dochi_yy] == '.':
                        data[dochi_xx][dochi_yy] = 'S'
                        dochi_queue.append([dochi_xx,dochi_yy])
            dochi_len-=1
    return "KAKTUS"
                        
            
R,C  = map(int,sys.stdin.readline().split())
data = []
for _ in range(R):
    data.append(list(sys.stdin.readline().strip()))

print(func())