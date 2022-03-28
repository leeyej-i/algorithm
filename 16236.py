# 백준 16236
# 골드 3 / 아기상어
from collections import deque
import sys

def bfs(second):
    global sharkX, sharkY, sharkSize, eatFish
    dx = [-1,0,1,0] 
    dy = [0,-1,0,1]
    queue = deque([[sharkX, sharkY]])
    visit = [[0 for _ in range(N)] for _ in range(N)]
    visit[sharkX][sharkY] = 1
    time = second
    fishes=[]
    while queue :
        time +=1
        for _ in range(len(queue)):
            x,y = queue.popleft()
            for i in range(4):
                xx = x+dx[i]
                yy = y+dy[i]
                if 0<=xx<N and 0<=yy<N:
                    if visit[xx][yy] == 0 :
                        if data[xx][yy] == 0 :
                            queue.append([xx,yy])
                            visit[xx][yy] = 1
                        elif data[xx][yy] == sharkSize :
                            queue.append([xx,yy])
                            visit[xx][yy] = 1
                        elif data[xx][yy] < sharkSize :
                            fishes.append([xx,yy])
                            visit[xx][yy] = 2
        if len(fishes) != 0:
            for i in range(N):
                for j in range(N):
                    if visit[i][j] == 2 :
                        eatFish +=1
                        if eatFish == sharkSize :
                            sharkSize+=1
                            eatFish = 0
                        sharkX,sharkY = i,j
                        data[i][j] = 0
                        return time
            
        
    return second

        
N = int(sys.stdin.readline().strip())
data = []
for _ in range(N) :
    data.append(list(map(int,sys.stdin.readline().split())))

sharkX, sharkY, sharkSize, eatFish = 0, 0, 2, 0
for i in range(N) :
    for j in range(N):
        if data[i][j] == 9 :
            sharkX, sharkY = i,j
            data[i][j] = 0

result = 0
while True :
    checkResult = result
    result = bfs(checkResult)
    if checkResult == result :
        break

print(result)