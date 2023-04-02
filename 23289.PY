# 백준 23289
# 플레티넘 5 / 온풍기 안녕!
import sys
from collections import deque
import copy

def wind(sx, sy, vector, cnt):
    visit[sx][sy] = cnt
    nsx = sx+dx[vector][0]
    nsy = sy+dy[vector][0]
    visit[nsx][nsy] = cnt
    room[nsx][nsy] += 5
    queue = deque()
    queue.append([nsx,nsy,5])
    while queue :
        x,y, temp = queue.popleft()
        for i in range(3):
            nx = x + dx[vector][i]
            ny = y + dy[vector][i]
            if 0<=nx<R and 0<=ny<C:
                # 벽이 있는 경우
                if vector == 0 : #오른쪽
                    if wall[nx][ny][1] == 1 :
                        continue
                    if i == 1 and wall[x][y][3] == 1 : continue
                    if i == 2 and wall[x][y][2] == 1 : continue
                elif vector == 1 : #왼쪾
                    if wall[nx][ny][0] == 1 :
                        continue
                    if i == 1 and wall[x][y][3] == 1 : continue
                    if i == 2 and wall[x][y][2] == 1 : continue
                elif vector == 2 : #위
                    if wall[nx][ny][3] == 1 :
                        continue
                    if i == 1 and wall[x][y][0] == 1 : continue
                    if i == 2 and wall[x][y][1] == 1 : continue
                else : # 아래
                    if wall[nx][ny][2] == 1  :
                        continue
                    if i == 1 and wall[x][y][0] == 1 : continue
                    if i == 2 and wall[x][y][1] == 1 : continue
                if visit[nx][ny] == cnt :
                    continue
                visit[nx][ny] = cnt
                room[nx][ny] += (temp -1)
                if temp -1 == 1 :
                    continue
                queue.append([nx,ny,temp-1])
                
def control():
    new_room = copy.deepcopy(room)
    for i in range(R):
        for j in range(C):
            if i+1 < R and j < C :
                if wall[i+1][j][2] != 1:
                    if room[i][j] >= room[i+1][j] :
                        dif = (room[i][j] - room[i+1][j])//4
                        new_room[i][j] -= dif
                        new_room[i+1][j] += dif
                    else :
                        dif = (room[i+1][j] - room[i][j])//4
                        new_room[i+1][j] -= dif
                        new_room[i][j] += dif
            if i<R and j+1<C :
                if wall[i][j+1][1] != 1 :
                    if room[i][j] >= room[i][j+1] :
                        dif = (room[i][j] - room[i][j+1])//4
                        new_room[i][j] -= dif
                        new_room[i][j+1] += dif
                    else :
                        dif = (room[i][j+1] - room[i][j])//4
                        new_room[i][j+1] -= dif
                        new_room[i][j] += dif
    return new_room
    
def minus():

    for i in range(R):
        if room[i][0] >= 1 : room[i][0] -= 1
        if room[i][C-1] >= 1 : room[i][C-1] -= 1
    for j in range(1,C-1):
        if room[0][j] >= 1 : room[0][j] -= 1
        if room[R-1][j] >= 1 : room[R-1][j]-=1

def check():
    for i,j in check_list:
        if room[i][j] < K :
            return False
    return True
            
    
# R * C / 최소 온도 K
R,C,K = map(int,sys.stdin.readline().split())


# 0: 빈 칸
# 1: 방향이 오른쪽인 온풍기가 있음
# 2: 방향이 왼쪽인 온풍기가 있음
# 3: 방향이 위인 온풍기가 있음
# 4: 방향이 아래인 온풍기가 있음
# 5: 온도를 조사해야 하는 칸
room = []
for _ in range(R):
    room.append(list(map(int,sys.stdin.readline().split())))

# 오른쪽, 왼쪽 위, 아래
mac = [[]for _ in range(4)]
check_list = []
for i in range(R):
    for j in range(C):
        if room[i][j] == 1 :
            mac[0].append([i,j])
        elif room[i][j] == 2 :
            mac[1].append([i,j])
        elif room[i][j] == 3 :
            mac[2].append([i,j])
        elif room[i][j] == 4 :
            mac[3].append([i,j])
        elif room[i][j] == 5 :
            check_list.append([i,j])
        room[i][j] = 0
    
# 벽 오 왼 위 아래
W = int(sys.stdin.readline().strip())
wall = [[[-1,-1,-1,-1] for _ in range(C)] for _ in range(R)]

# t가 0이면 x y 와 x-1 y / 1이면 x y 와 x y+1
for i in range(W):
    x,y,t = map(int,sys.stdin.readline().split())
    if t == 1 :
        wall[x-1][y-1][0] = 1
        wall[x-1][y][1] = 1
    else :
        wall[x-1][y-1][2] = 1
        wall[x-2][y-1][3] = 1
    
dx = [[0,1,-1],[0,1,-1],[-1,-1,-1],[1,1,1]]
dy = [[1,1,1],[-1,-1,-1],[0,1,-1],[0,1,-1]]
visit = [[0 for _ in range(C)] for _ in range(R)]

# 초콜렛 수
res = 0
tmp = 1
while(True):
    for k in range(4):
        for i,j in mac[k]:
            wind(i,j,k,tmp)
            tmp += 1
    # for item in room:
    #     print(item)
    # print()
    room = control()
    minus()
    res +=1
    if res > 100 :
        break
    if check():
        break
# for item in room:
#     print(item)
# print()
print(res)
