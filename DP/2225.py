# 백준 2225
# 골드 5 / 합 분해
import sys

N, K = map(int,sys.stdin.readline().split())


# K * N
dp = [[0 for _ in range(N + 1 )] for _ in range(K+ 1)]

for i in range(1, K+1) :
    for j in range(1, N+1) :
        if i == 1 : 
            dp[i][j] = 1
        elif j == 1 :
            dp[i][j] = i
        else :
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[K][N])