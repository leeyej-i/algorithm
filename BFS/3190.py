# 백준 3190
# 골드 5 / 뱀
from collections import deque
import sys        

def func():
    check = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    check_index = 0
    snack = deque()
    snack.append([0,0])
    cnt = 0
    for item in switches:
        second, vector = int(item[0]), item[1]
        second -= cnt
        while second:
            current_x, current_y = snack.pop()
            next_x = current_x + check[check_index][0]
            next_y = current_y + check[check_index][1]
            snack.append([current_x, current_y])
            cnt += 1
            if next_x == -1 or next_x == N or next_y == -1 or next_y == N:
                return cnt
            if board[next_x][next_y] == 2:
                snack.append([next_x,next_y])
                board[next_x][next_y] = 1
            elif board[next_x][next_y] == 1:
                return cnt
            elif board[next_x][next_y] == 0:
                board[next_x][next_y] = 1
                snack.append([next_x, next_y])
                delete_x, delete_y = snack.popleft()
                board[delete_x][delete_y] = 0
            second -= 1
        if vector == 'L':
            check_index -= 1
            if check_index == -1:
                check_index = 3
        elif vector == 'D':
            check_index += 1
            if check_index == 4:
                check_index = 0
    while True:
            current_x, current_y = snack.pop()
            next_x = current_x + check[check_index][0]
            next_y = current_y + check[check_index][1]
            snack.append([current_x, current_y])
            cnt += 1
            if next_x == -1 or next_x == N or next_y == -1 or next_y == N:
                return cnt
            if board[next_x][next_y] == 2:
                snack.append([next_x,next_y])
                board[next_x][next_y] = 1
            elif board[next_x][next_y] == 1:
                return cnt
            elif board[next_x][next_y] == 0:
                board[next_x][next_y] = 1
                snack.append([next_x, next_y])
                delete_x, delete_y = snack.popleft()
                board[delete_x][delete_y] = 0
        
     
N = int(sys.stdin.readline().strip())
apple = int(sys.stdin.readline().strip())
board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(apple):
    apple_x, apple_y = map(int,sys.stdin.readline().split())
    board[apple_x-1][apple_y-1] = 2 #사과 번호 = 2
switch = int(sys.stdin.readline().strip())
switches = []
for _ in range(switch):
    switches.append(list(sys.stdin.readline().split()))
board[0][0] = 1 #뱀 번호 = 1
print(func())
