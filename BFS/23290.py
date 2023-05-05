# 백준 23290
# 골드 1 / 마법사 상어와 복제
import sys
import copy


# 물고기 복제
def copyFish(fish_copy) :
    global fish
    for i in range(4):
        for j in range(4):
            fish[i][j] += (fish_copy[i][j])

#물고기 이동             
def moveFish():
    global fish
    new_fish = [[[]for _ in range(4)] for _ in range(4)]
    #  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
    dx = [0,-1,-1,-1,0,1,1,1]
    dy = [-1,-1,0,1,1,1,0,-1]
    for i in range(4):
        for j in range(4):
            while fish[i][j]:
                vector = fish[i][j].pop()
                move = 0 #움직인 여부 확인
                for _ in range(8):
                    new_x = dx[vector] + i
                    new_y = dy[vector] + j
                    rotation = 0
                    # 격자를 벗어나면 반시계 방향
                    if new_x < 0 or new_x >= 4 or new_y<0 or new_y >=4 :
                        rotation = 1
                    else: 
                        # 상어가 있는 위치면 반시계
                        if new_x == sx and new_y == sy:
                            rotation = 1
                        # 냄새가 나는 구역이면 반시계
                        if smell[new_x][new_y] > 0:
                            rotation = 1
                    # 반시계로 돌아야 하면
                    if rotation == 1 :
                        vector -= 1
                        if vector == -1 :
                           vector = 7
                    # 안돌아도 바로 갈 수 있으면
                    else :
                        new_fish[new_x][new_y].append(vector)
                        move = 1
                        break
                #움직이지 않았으면 그 자리에 추가
                if move == 0 :
                    new_fish[i][j].append(vector)
    return new_fish


# 상어 이동
def moveShark(x, y, dept, cnt, visit):
    global fish, max_fish, sx, sy, eat_list
    # 3번 움직였으면 종료문
    if dept == 3 :
            if max_fish < cnt :
                max_fish = cnt
                sx, sy = x, y
                eat_list = copy.deepcopy(visit)
            return
        
    for i in range(4):
        new_x, new_y = x + s_dx[i], y + s_dy[i]
        if 0<=new_x<4 and 0<=new_y<4:
            if [new_x, new_y] not in visit:
                visit.append([new_x, new_y])
                eat_fish = len(fish[new_x][new_y])
                moveShark(new_x, new_y, dept+1, cnt +eat_fish, visit)
                visit.pop()
            # 상어가 방문했던 곳도 다시 봐야 함(상어위치에 복제된 물고기가 있을 수도 있기 때문)
            # ex) 상어가 위의 물고기 먹음 -> 원래 위치의 물고기를 먹기 위해 내려옴 -> 그 주변에 물고기가 없어서 위로가는게 사전상 좋을 때
            else: 
                 moveShark(new_x, new_y, dept+1, cnt, visit)
            
                     
# 물고기 수, 상어 마법 연습 횟수 S
M, S = map(int,sys.stdin.readline().split())

fish = [[[]for _ in range(4)] for _ in range(4)]
smell = [[0 for _ in range(4)]for _ in range(4)]
s_dx = [-1, 0, 1, 0]
s_dy = [0, -1, 0, 1]
for _ in range(M):
    fx, fy, d= map(int,sys.stdin.readline().split())
    fish[fx-1][fy-1].append(d-1)
    
sx, sy = map(int,sys.stdin.readline().split())
sx,sy = sx-1, sy-1


# S번의 연습
for _ in range(S):
    fish_copy = copy.deepcopy(fish)
    fish = copy.deepcopy(moveFish())
    # for item in fish :
    #     print(item)
    # print()
    max_fish = -1
    eat_list = []
    moveShark(sx, sy, 0, 0, [])
    # for item in fish :
    #     print(item)
    # print()
    for x, y in eat_list :
        if fish[x][y] :
            fish[x][y] = []
            smell[x][y] = 3
    copyFish(fish_copy)
    # for item in fish :
    #     print(item)
    # print()
    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                smell[i][j]-=1
    
res =0
for i in range(4):
    for j in range(4):
        res += len(fish[i][j])

print(res)