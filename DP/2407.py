# 백준 2407
# 실버 3 / 조합
import sys

n, m = map(int,sys.stdin.readline().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if j==0 : 
            dp[i][j] = 1
            continue
        if j==1: 
            dp[i][j] = i
            continue
        if i == j : 
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[n][m])