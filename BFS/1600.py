# 백준 1600
# 골드 4 / 말이 되고픈 원숭이
from collections import deque
import sys

def bfs():
    dx1 = [0,0,1,-1]
    dy1 = [1,-1,0,0]
    dx2 = [1,1,-1,-1,2,2,-2,-2]
    dy2 = [2,-2,2,-2,1,-1,1,-1]
    queue = deque()
    queue.append([0,0])
    data[0][0] = 0
    time=0
    while queue :
        for _ in range(len(queue)):
            x,y= queue.popleft()
            if x==H-1 and y==W-1 :
                return time
            for i in range(4):
                xx = x + dx1[i]
                yy = y + dy1[i]
                if 0<=xx<H and 0<=yy<W :
                    if data[xx][yy] == -1:
                        queue.append([xx,yy])
                        data[xx][yy] = data[x][y]
                    elif data[xx][yy] > data[x][y] :
                        queue.append([xx,yy])
                        data[xx][yy] = data[x][y]
            if data[x][y]<K :
                for i in range(8) :
                    xx = x + dx2[i]
                    yy = y + dy2[i]
                    if 0<=xx<H and 0<=yy<W :
                        if data[xx][yy] == -1:
                            queue.append([xx,yy])
                            data[xx][yy] = data[x][y]+1
                        elif data[xx][yy] > data[x][y]+1 :
                            queue.append([xx,yy])
                            data[xx][yy] = data[x][y]+1
        time+=1
    return -1
K = int(sys.stdin.readline().strip())
W,H = map(int,sys.stdin.readline().split())
data = []
for _ in range(H):
    data.append(list(map(int,sys.stdin.readline().split())))
for i in range(H):
    for j in range(W):
        if data[i][j] == 0 :
            data[i][j] = -1
        else :
            data[i][j] = -2 
print(bfs())
