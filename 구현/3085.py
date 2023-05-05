# 백준 3085
# 실버 3 / 사탕게임
import sys
N=int(sys.stdin.readline())
board=[]
for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

def func(board):
    result=1
    for i in range(N):
        cnt = 1
        for j in range(1,N):
            if board[i][j] == board[i][j-1]:
                cnt +=1
                result = max(result, cnt)
            else :
                cnt=1
        cnt = 1
        for j in range(1,N):
            if board[j][i] == board[j-1][i]:
                cnt +=1
                result = max(result, cnt)
            else :
                cnt=1
    return result

res=1
for i in range(N):
    for j in range(N):
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            sub_result = func(board)
            res = max(sub_result,res)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        
        if i+1 < N :
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            sub_result = func(board)
            res = max(sub_result,res)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(res) 