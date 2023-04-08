# 백준 21611
# 골드 1 / 마법사 상어와 블리자드
import sys
from collections import deque
import copy
def blizzard(d,s, shark):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    nx, ny = shark[0], shark[1]
    for _ in range(s):
        nx = nx + dx[d]
        ny = ny + dy[d]
        data[nx][ny] = 0
        
def move(shark):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    vector = 0
    x, y = shark[0], shark[1]
    nx, ny = x, y
    move_list = deque()
    for i in range(1,N):
        for j in range(3):
            for _ in range(i):
                nx,ny = nx+dx[vector], ny + dy[vector]
                if data[x][y] != 0 :
                    x, y = nx, ny
                else :
                    if data[nx][ny] != 0:
                        move_list.append([nx, ny])
                        data[x][y] = data[nx][ny]
                        data[nx][ny] = 0
                        x, y = move_list[0][0], move_list[0][1]
                        move_list.popleft()
                    else :
                        move_list.append([nx,ny])
            vector += 1
            if vector == 4 : vector = 0 
            if i != N - 1 and j==1 :
                break
            
def explode(shark) :
    global result
    res = False
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    vector = 0
    x, y = shark[0], shark[1]
    nx, ny = x, y
    check_list = []
    for i in range(1,N):
        for j in range(3):
            for _ in range(i):
                nx,ny = x+dx[vector], y + dy[vector]
                if data[nx][ny] == data[x][y] :
                    check_list.append([nx,ny])
                else :
                    if len(check_list) >= 4 :
                        for cx, cy in check_list :
                            result += data[cx][cy]
                            data[cx][cy] = 0
                            res = True
                    check_list = [[nx,ny]]
                x, y = nx,ny
            vector += 1
            if vector == 4 : vector = 0 
            if i != N - 1 and j==1 :
                break
    return res
        
def change(shark):
    res = []
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    vector = 0
    x, y = shark[0], shark[1]
    nx, ny = x, y
    check_list = []
    for i in range(1,N):
        for j in range(3):
            for _ in range(i):
                nx,ny = x+dx[vector], y + dy[vector]
                if data[nx][ny] == data[x][y] :
                    check_list.append([nx,ny])
                else :
                    if len(check_list) > 0 :
                        res.append(len(check_list))
                        res.append(data[x][y])
                    check_list = [[nx,ny]]
                x, y = nx,ny
            vector += 1
            if vector == 4 : vector = 0 
            if i != N - 1 and j==1 :
                break

    vector = 0
    data_copy = [[0 for _ in range(N)] for _ in range(N)]
    data_copy[shark[0]][shark[1]] = -1
    x, y = shark[0], shark[1]
    nx, ny = x, y
    index = 0
    for i in range(1,N):
        for j in range(3):
            for _ in range(i):
                nx,ny = x+dx[vector], y + dy[vector]
                data_copy[nx][ny] = res[index]
                index +=1
                if index == len(res) :
                    return data_copy
                x, y = nx,ny
            vector += 1
            if vector == 4 : vector = 0 
            if i != N - 1 and j==1 :
                break
    return data_copy
            
def checkNull():
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0 and data[i][j] != -1 :
                return False
    return True

N, M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

magic= []
result = 0
for _ in range(M):
    # 방향(위 아래 왼 오 1 2 3 4), 거리
    d, s = map(int,sys.stdin.readline().split())
    magic.append([d-1,s])

shark = [(N+1)//2 -1, (N+1)//2-1]
data[shark[0]][shark[1]] = -1
for d, s in magic :
    blizzard(d,s, shark)
    move(shark)
    # print("움직이기")
    # for item in data:
    #     print(item)
    while True :
        if explode(shark) == False:
            break
        move(shark)
    if checkNull() :
        break
    data = change(shark)
    # print("바꾸기")
    # for item in data:
    #     print(item)

print(result)