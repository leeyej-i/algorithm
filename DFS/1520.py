# 백준 1520
# 골드 4 / 내리막길
import sys
sys.setrecursionlimit(10**6)

def dfs(x,y) :
    if x==N-1 and y==M-1 :
        return 1
    dp[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<N and 0<=yy<M :
            if data[xx][yy] < data[x][y]:
                if dp[xx][yy] == -1 :
                    dp[x][y] += dfs(xx,yy)
                else :
                    dp[x][y] += dp[xx][yy]
    return dp[x][y]
                
N, M = map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

dp = [[-1 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dfs(0,0)
print(dp[0][0])