# 백준 15489
# 실버 4 / 파스칼 삼각형
import sys

R,C,W = map(int,sys.stdin.readline().split())

data = [[0 for _ in range(R+W)] for _ in range(R+W)]

data[1][1] = 1
for i in range(1,R+W):
    for j in range(1,R+W):
        if i == 1 and j == 1 : continue
        data[i][j] = data[i-1][j] + data[i-1][j-1]

res = 0
temp = R
for j in range(C, C+W):
    for i in range(temp, R+W):
        res += data[i][j]
    temp+=1
        
print(res)