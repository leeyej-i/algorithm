# 백준 2615
# 실버 2 / 오목
import sys
def func(value, i, j):
    result = 0
    if i+1 < 19 and j+1<19:
        if board[i+1][j+1] == value:
            result = max(result,func2(0,i,j,value))
    if i+1 < 19:
        if board[i+1][j]== value:
            result = max(result,func2(1,i,j,value))
    if j+1 < 19 :
        if board[i][j+1] == value:
            result = max(result,func2(2,i,j,value))
    if i-1 > 0 and j+1 <19:
        if board[i-1][j+1] == value:
            result = max(result,func2(3,i,j,value))
    if result == 5 :
        return 1 
    else: 
        return 0

def func2(case, i, j, value):
    cnt = 0
    if case == 0 :
        if i!= 0 and j!=0:
            if board[i-1][j-1] == value :
                return 0
        while board[i][j] == value :
            cnt +=1
            i+=1
            j+=1
            if i == 19 or j==19 :
                break
    elif case == 1 :
        if i!= 0 :
            if board[i-1][j] == value :
                return 0
        while board[i][j] == value :
            cnt +=1
            i+=1
            if i == 19:
                break
    elif case == 2 :
        if j!=0:
            if board[i][j-1] == value :
                return 0
        while board[i][j] == value :
            cnt +=1
            j+=1
            if j  == 19 :
                break
    elif case == 3 :
        if i!=18 and j!=0:
            if board[i+1][j-1] == value :
                return 0
        while board[i][j] == value :
            cnt +=1
            i-=1
            j+=1
            if i == -1 or j == 19 :
                break
    if cnt == 5:
        return 5
    else :
        return 0

board = []
for _ in range(19):
    board.append(list(map(int,sys.stdin.readline().split())))

for i in range(19):
    for j in range(19):
        if board[i][j] == 1 or board[i][j] == 2:
            if func(board[i][j], i, j) :
                print(board[i][j])
                print("%d %d"%(i+1,j+1))
                exit()
print(0)