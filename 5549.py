# 백준 5549
# 골드 5 / 행성탐사
import sys
N, M = map(int,sys.stdin.readline().split())
K = int(sys.stdin.readline().strip())

map_list = []
for _ in range(N) :
    map_list.append(list(sys.stdin.readline().strip()))

# J 정글, O 바다, I 얼음
sum_list = [[[0,0,0] for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        for k in range(3):
            sum_list[i+1][j+1][k] = sum_list[i+1][j][k] + sum_list[i][j+1][k] - sum_list[i][j][k]
        if map_list[i][j] == "J":
            sum_list[i+1][j+1][0] += 1
        if map_list[i][j] == "O":
             sum_list[i+1][j+1][1] += 1
        if map_list[i][j] == "I":
             sum_list[i+1][j+1][2] += 1

for _ in range(K):
    a, b, c, d = map(int, sys.stdin.readline().split())
    result = [0,0,0]
    for i in range(3):
        result[i] = sum_list[c][d][i] - sum_list[c][b-1][i] - sum_list[a-1][d][i] + sum_list[a-1][b-1][i]
    print(*result)