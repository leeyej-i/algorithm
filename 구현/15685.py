# 백준 15685
# 골드 4 / 드래곤 커브
from collections import deque
import sys

def dragonCurv(x,y,d,g) :
    graph[y][x] = 1
    curvArray=[[x,y]]
    if d == 0 :
        x=x+1
    elif d == 1 :
        y=y-1
    elif d == 2 :
        x=x-1
    else :
        y=y+1
    graph[y][x] = 1
    curvArray.append([x,y])
    cnt = 0
    while True :
        x = curvArray[len(curvArray)-1][0]
        y = curvArray[len(curvArray)-1][1]
        cnt+=1
        if cnt == g+1 :
            break
        length = len(curvArray)
        for i in range(length):
            checkX, checkY = curvArray[length-i-1][0], curvArray[length-i-1][1]
            if checkX == x and checkY == y :
                continue
            xx = x-(checkY-y)
            yy = y+(checkX-x)
            if 0<=xx<=100 and 0<=yy<=100:
                graph[yy][xx] = 1
                curvArray.append([xx,yy])
                      
        
N= int(sys.stdin.readline().strip())
graph = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    x, y, d, g  = map(int,sys.stdin.readline().split())
    dragonCurv(x,y,d,g)

result=0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            if graph[i+1][j+1] == 1 and graph[i+1][j] ==1 and graph[i][j+1] == 1 :
                result+=1
            
print(result)