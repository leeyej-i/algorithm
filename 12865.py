# 백준 12865
# 골드 5 / 평범한 배낭
import sys
N, K = map(int,sys.stdin.readline().split())
w=[0 for _ in range(N+1)]
v=[0 for _ in range(N+1)]
for i in range(1,N+1):
    weight, value = map(int,sys.stdin.readline().split())
    w[i],v[i] = weight, value
    
#다이나믹 프로그래밍
dp=[[0 for _ in range(K+1)]for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,K+1):
        if j < w[i] :
            dp[i][j] = dp[i-1][j]
        else :
            dp[i][j] = max(v[i] + dp[i-1][j-w[i]], dp[i-1][j])

print(dp[N][K])