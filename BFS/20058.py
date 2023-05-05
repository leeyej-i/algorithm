# 백준 20058
# 골드 3 / 마법사 상어와 파이어스톰

import sys
from collections import deque

def switch(num):
    global a_list
    d_num = 2**num
    # 임시 판
    d_list = [[0 for _ in range(2**N)] for _ in range(2**N)]
    # 전체 판에서
    for i in range(0, 2**N, d_num):
        for j in range(0, 2**N, d_num):
            # d_num만큼씩 나눠서 돌리기
            for k in range(d_num): 
                for l in range(d_num): 
                    d_list[i + k][j + l] = a_list[i + d_num-l-1][j+k]
    a_list = d_list
    
def melt():
    # 녹아야하는 부분 체크리스트
    check_meliting = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            if a_list[i][j] > 0 :
                for k in range(4):
                    ii = i + dx[k]
                    jj = j + dy[k]
                    if 0<= ii< 2**N and 0<= jj < 2**N :
                        if a_list[ii][jj] > 0 :
                            cnt += 1
                if cnt < 3 :
                    check_meliting[i][j] = 1
    for i in range(2**N):
        for j in range(2**N):
            if check_meliting[i][j] == 1 :
                a_list[i][j] -= 1
                    


def count_big(x, y):
    cnt = 1
    queue = deque()
    queue.append([x,y])
    while(queue):
        xx, yy = queue.pop()
        for k in range(4):
            xxx = xx + dx[k]
            yyy = yy + dy[k]
            if 0<= xxx< 2**N and 0<= yyy < 2**N and visit[xxx][yyy] == 0:
                if a_list[xxx][yyy] > 0 :
                    cnt += 1
                    visit[xxx][yyy] = 1
                    queue.append([xxx,yyy])
    
    return cnt


N, Q = map(int,sys.stdin.readline().split())
a_list = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for _ in range(2**N):
    a_list.append(list(map(int, sys.stdin.readline().split())))

l_list = list(map(int,sys.stdin.readline().split()))

for i in range(Q):
    if l_list[i] > 0 :
        switch(l_list[i])
    melt()

res1, res2 = 0, 0
for item in a_list :
    res1 += sum(item)
    
visit = [[0 for _ in range(2**N)] for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if visit[i][j] == 0 and a_list[i][j] > 0:
            visit[i][j] = 1
            res2 = max(res2, count_big(i, j))


print(res1)
print(res2)