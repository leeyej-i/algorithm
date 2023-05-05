# 백준 9663
# 골드 5 / N-Queen
from itertools import permutations
import sys

def canAttack(i, row):
    for j in range(1,row+1):
            if abs(i - checkRow[row-j]) == j :
                return 0
    return 1

def back(row):
    global result
    if row == N :
        result+=1
        return
    for i in range(N):
        if checkCol[i] == 0:
            if canAttack(i, row) :
                checkRow[row] = i
                checkCol[i] = 1
                back(row+1)
                checkCol[i] = 0
            
N = int(sys.stdin.readline().strip())
result = 0
checkRow = [-1 for _ in range(N)]
checkCol = [0 for _ in range(N)]
back(0)
print(result)