# 백준 17142
# 골드 4 / 연구소 3
from collections import deque
from itertools import combinations
import sys

#bfs 함수
def bfs(array) :
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue = deque(array)
    visit = [[0 for _ in range(N)] for _ in range(N)]
    for item in array :
        visit[item[0]][item[1]] = 1
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                visit[i][j] = -1
                
    #비활성화 바이러스 방문 체크를 위한 배열            
    disableVirus = [[0 for _ in range(N)] for _ in range(N)]
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<N and 0<=yy<N :
                if visit[xx][yy] == 0:
                    if data[xx][yy] == 2 : #비활성화 바이러스 일경우
                        visit[xx][yy] = visit[x][y]
                        queue.append([xx,yy])
                        if disableVirus[x][y] !=0 : # 2 -> 2
                            disableVirus[xx][yy] = disableVirus[x][y]+1
                        else : # 1 -> 2
                            disableVirus[xx][yy] = visit[x][y] + 1
                    else : # 빈칸
                        if disableVirus[x][y] != 0 : # 2 -> 1
                            visit[xx][yy] = disableVirus[x][y] + 1
                        else : # 1 -> 1
                            visit[xx][yy] = visit[x][y] + 1
                        queue.append([xx,yy])
    
    time = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 :
                return -1
            time = max(time, visit[i][j])
    return time-1

N,M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N) :
    data.append(list(map(int,sys.stdin.readline().split())))

virus = []
for i in range(N) :
    for j in range(N):
        if data[i][j] == 2 :
            virus.append([i,j])

            
result = -1
for i in combinations(virus, M) :
    bfsResult = bfs(i)
    if result == -1 :
        if bfsResult != -1:
            result = bfsResult
    else :
        if bfsResult != -1:
            result = min(result, bfsResult)

print(result)