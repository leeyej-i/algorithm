# 백준 9944
# 골드 3 / N*M보드 완주하기
import sys
sys.setrecursionlimit(10**7)

# 한 방향으로 쭉 가기
# def go (x,y,vector):
#     board_list = [[x, y]]
#     while True:
#         x, y = x + dx[vector], y + dy[vector]
#         if 0<=x<N and 0<=y<M :
#             if board[x][y] == '.':
#                 board[x][y] = '*'
#                 board_list.append([x,y])
#             else :
#                 break
#         else :
#             break
#     return board

# 왔던 방향 되돌아가기
# def back(go_list) :
#     for x,y in go_list :
#         board[x][y] = '.'

# 다 방문했는지 확인
def full_check():
    for i in range(N):
        for j in range(M):
            if board[i][j] == '.':
                return False
    return True

# 비어있는 칸 각각에서 백트래킹            
def solve(x,y, stage) :
    global res
    if full_check() :
        res = min(res, stage)
    if stage < res:
        for i in range(4):
            go_list = []
            nx, ny = x, y
            while True:
                nx, ny = nx + dx[i], ny + dy[i]
                if 0<=nx<N and 0<=ny<M and board[nx][ny] == '.':
                    go_list.append([nx,ny])
                    board[nx][ny] = '*'
                else :
                    break
            if go_list :
                solve(nx-dx[i],ny-dy[i], stage+1)
            for a,b in go_list :
                board[a][b] = '.'
        board[x][y] = "." 
    
T = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
while (True):
    try :
        N, M = map(int,sys.stdin.readline().split())
        board = []
        for _ in range(N):
            board.append(list(sys.stdin.readline().strip()))
        res = float('inf')
        for i in range(N):
            for j in range(M):
                if board[i][j] == '.':
                    board[i][j] = '*'
                    # x, y, stage
                    solve(i,j,0) 
    
        if res == float('inf'):
            res = -1
        print("Case {}: {}".format(T,res))
        T+=1
    except :
        break