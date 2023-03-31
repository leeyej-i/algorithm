# 백준 1938
# 골드 2 / 통나무 옮기기
import sys
from collections import deque
def rotate(x,y,v):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0<=i<N and 0<=j<N and field[i][j] != '1':
                continue
            else :
                return [x,y,-1]
    if v==1 :
        v = 0
    else : v= 1
    return [x,y,v]

def work(x,y,v,i):
    nx, ny, nv = x,y,v
    if i == 0 : #상
        nx,ny,nv = nx-1, ny, v
        if nv == 0 : # 세로면 
            if nx-1 < 0 :  nv = -1
            elif field[nx-1][ny] == '1' : nv = -1
        else : # 가로면
            if nx < 0 : nv = -1
            elif field[nx][ny] == '1' or field[nx][ny-1] == '1' or field[nx][ny+1] == '1' : 
                nv = -1
    elif i == 1: #하
        nx,ny,nv = nx+1, ny, v
        if nv == 0 : # 세로면 
            if nx+1 >= N :  nv = -1
            elif field[nx+1][ny] == '1' : nv = -1
        else : # 가로면
            if nx >= N : nv = -1
            elif field[nx][ny] == '1' or field[nx][ny-1] == '1' or field[nx][ny+1] == '1' : 
                nv = -1
    elif i == 2: #좌
        nx,ny,nv = nx, ny-1, v
        if nv == 0 : # 세로면 
            if ny < 0 :  nv = -1
            elif field[nx][ny] == '1' or field[nx-1][ny] == '1' or field[nx+1][ny] == '1' :
                nv = -1 
        else : # 가로면
            if ny -1 < 0: nv = -1
            elif field[nx][ny-1] == '1' : nv = -1
    elif i == 3: #우
        nx,ny,nv = nx, ny+1, v
        if nv == 0 : # 세로면 
            if ny >= N :  nv = -1
            elif field[nx][ny] == '1' or field[nx-1][ny] == '1' or field[nx+1][ny] == '1' :
                nv = -1 
        else : # 가로면
            if ny +1 >= N: nv = -1
            elif field[nx][ny+1] == '1' : nv = -1
    elif i == 4: #회전
        nx,ny,nv = rotate(x,y,v)
    return [nx,ny,nv]
    
# 중간 위치의 좌표 x, y, 방향
# v가 0이면 세로, 1이면 가로
def solve(sx, sy, sv):
    queue = deque()
    queue.append([sx,sy,sv,0])
    while queue:
        x,y,v,cnt = queue.popleft()
        for i in range(5):
            nx, ny, nv = x,y,v
            nx, ny, nv = work(x,y,v,i)
            if nv == -1 : continue
            if visit[nx][ny][nv] == -1 :
                visit[nx][ny][nv] = cnt + 1
                queue.append([nx,ny,nv,cnt+1])
            elif visit[nx][ny][nv] == -2 :
                print(cnt+1)
                exit()
            elif visit[nx][ny][nv] <= cnt + 1:
                continue
    print(0)
    exit()

N = int(sys.stdin.readline().strip())

field = []
for _ in range(N):
    field.append(list(sys.stdin.readline().strip()))

start = [] # 시작 통나무위치
finish = [] # 끝 통나무위치
for i in range(N) : 
    for j in range(N):
        if field[i][j] == 'B':
           start.append([i,j])
        elif field[i][j] == 'E' :
            finish.append([i,j])

#통나무가 세로로 놓여져있을 때는 0번째
#통나무가 가로로 놓여져있을 때는 1번째
visit = [[[-1,-1] for _ in range(N)] for _ in range(N)]
start_v = 0
if start[0][0] == start[1][0]:
    visit[start[1][0]][start[1][1]][1] = 0
    start_v = 1
else :
    visit[start[1][0]][start[1][1]][0] = 0
    

# 도착위치는 -2로 표시
if finish[0][0] == finish[1][0]:
    visit[finish[1][0]][finish[1][1]][1] = -2
else :
    visit[finish[1][0]][finish[1][1]][0] = -2

solve(start[1][0], start[1][1], start_v)

    