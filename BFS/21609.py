# 백준 21609
# 골드 2 / 상어 중학교
import sys
import copy
from collections import deque
def bfs(sx,sy) :
    rainbow_list = []
    block_list = [[sx,sy]]
    color = data[sx][sy]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append([sx,sy])
    visit[sx][sy] = 1
    while queue : 
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0 :
                if data[nx][ny] == color:
                    queue.append([nx,ny])
                    visit[nx][ny] = 1
                    block_list.append([nx,ny])
                if data[nx][ny] == 0 :
                    queue.append([nx,ny])
                    rainbow_list.append([nx,ny])
                    visit[nx][ny] = 1
                    block_list.append([nx,ny])
    for rx, ry in rainbow_list :
        visit[rx][ry] = 0
    return [block_list, len(rainbow_list)]

def check_block(): 
    global big_block , r_num
    for i in range(N):
        for j in range(N):
            if data[i][j] == -1 : # 검정 블록
                continue
            elif data[i][j] == 0 : # 무지개블록
                continue
            elif data[i][j] == -2 : # 빈 곳
                continue
            else :
                if visit[i][j] == 0 :
                    block_list, nr_num = bfs(i,j)
                    if len(block_list) > len(big_block):
                        big_block = block_list
                        r_num = nr_num
                    elif len(block_list) == len(big_block):
                        if r_num <= nr_num :
                            big_block = block_list
                            r_num = nr_num

    for bx, by in big_block :
        data[bx][by] = -2
    return len(big_block)**2

def gravity():
    for j in range(N):
        group = []
        for i in range(N):
            if data[i][j] == -1 :
                group = []
                continue
            elif data[i][j] == -2 :
                cx = i
                for l in range(len(group)-1, -1, -1) :
                    x = group[l]
                    data[cx][j] = data[x][j]
                    group[l] = cx
                    cx = x
                if group :
                    data[group[0]-1][j] = -2                    
            else :
                group.append(i)

N, M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))


score = 0
while True :
    big_block = []
    r_num = 0
    visit = [[0 for _ in range(N)]for _ in range(N)]
    check = check_block()
    if check == 0 or check == 1:
        break
    score += check
    # print("bfs")
    # for iten in data:
    #     print(iten) 
    # print()
    # print(score)
    gravity()
    # print("중력")
    # for iten in data:
    #     print(iten) 
    # print()
    # rotate
    new_list = list(map(list, zip(*data)))[::-1]
    data = new_list
    # print("회전")
    # for iten in data:
    #     print(iten) 
    # print()
    gravity()
    # print("중력")
    # for iten in data:
    #     print(iten) 
    # print()
print(score)