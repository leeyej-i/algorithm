# 백준 10159
# 골드 4 / 저울
import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

data = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    data[a][b] = 1 

# 플로이드-워셜
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if data[i][k] == 1 and data[k][j] == 1 :
                data[i][j] = 1

for i in range(1, N+1) :
    res = 0
    for j in range(1, N+1):
        if i == j :
            continue
        if data[i][j] == 0 and data[j][i] == 0:
            res +=1 
    print(res) 

