# 백준 1655
# 골드 5 / 적록색약
from collections import deque
import sys

def bfs1(first_x, first_y):
    queue = deque()
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue.append([first_x,first_y])
    check = data[first_x][first_y]
    visit[first_x][first_y] = 1
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<N and 0<=yy<N :
                if visit[xx][yy] == 0 and data[xx][yy] == check:
                    visit[xx][yy] = 1
                    queue.append([xx,yy])
                     
def bfs2(first_x, first_y):
    queue = deque()
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    queue.append([first_x,first_y])
    visit2[first_x][first_y] = 1
    checks=[]
    if data[first_x][first_y]== 'R' or data[first_x][first_y] == 'G':
        checks.append('R')
        checks.append('G')
    else :
        checks.append('B')
    while queue :
        x,y = queue.popleft()
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<N and 0<=yy<N :
                if visit2[xx][yy] == 0 and data[xx][yy] in checks:
                    visit2[xx][yy] = 1
                    queue.append([xx,yy])
                     
N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(sys.stdin.readline().strip()))
visit = [[0 for _ in range(N)]for _ in range(N)]
visit2= [[0 for _ in range(N)]for _ in range(N)]
result1, result2 = 0,0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 :
            bfs1(i,j)
            result1+=1
        if visit2[i][j] == 0 :
            bfs2(i,j)
            result2+=1

print(result1, end=' ')
print(result2)