# 백준 11559
# 골드 4 / Puyo Puyo
from collections import deque
import sys
data= []
for _ in range(12):
    data.append(list(sys.stdin.readline().strip()))

result = 0
while True :
    visit=[[0 for _ in range(6)] for _ in range(12)]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    popData = []
    for h in range(12):
        for z in range(6):
            queue = deque()
            if data[h][z] != '.' and visit[h][z] == 0 :
                queue.append([h,z])
                visit[h][z] = 1
                cnt=1
                while queue :
                    x,y= queue.popleft()
                    for i in range(4):
                        xx = x+dx[i]
                        yy = y+dy[i]
                        if 0<=xx<12 and 0<=yy<6:
                            if visit[xx][yy] == 0:
                                if data[xx][yy] == data[x][y]:
                                    visit[xx][yy] = 1
                                    queue.append([xx,yy])
                                    cnt+=1
                                elif data[xx][yy] == '.':
                                    visit[xx][yy] = -1
                    if cnt >= 4 :
                        popData.append([x,y])
                        break
    
    if len(popData) > 0 :
        result+=1
        popItem = []
        for i,j in popData:
            queue2 = deque([[i,j]])
            popItem.append([i,j])
            visit[i][j] = 2
            value = data[i][j]
            while queue2 :
                x,y = queue2.popleft()
                for l in range(4) :
                    xx = x+dx[l]
                    yy = y+dy[l]
                    if 0<=xx<12 and 0<=yy<6 and visit[xx][yy] == 1:
                        if data[xx][yy] == value:
                            popItem.append([xx,yy])
                            queue2.append([xx,yy])
                            visit[xx][yy] = 2
        popItem.sort()
        for i, j in popItem:
            for k in range(i, 0, -1):
                data[k][j] = data[k-1][j]
            data[0][j] = '.'
    else :
        break
                            
print(result)
                            
                        
                        
    