# 백준 1890
# 실버 1 / 점프
import sys

N = int(sys.stdin.readline().strip())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    
visit = [[0 for _ in range(N)] for _ in range(N)]
visit[0][0] = 1

for i in range(N):
    for j in range(N):
        if i==N-1 and j == N-1 : continue
        if visit[i][j] != 0:
            nx = i + data[i][j]
            ny = j + data[i][j]
             
            if nx < N :
                visit[nx][j] += visit[i][j]
            
            if ny < N :
                visit[i][ny] += visit[i][j]

print(visit[N-1][N-1])