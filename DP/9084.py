# 백준 9084
# 골드 5 / 동전
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip()) #동전의 종류
    coins=list(map(int,sys.stdin.readline().split())) # 동전 배열
    M = int(sys.stdin.readline().strip()) #만들어야 할 목표
    dp=[[0 for _ in range(M+1)]for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,M+1):
            if j < coins[i-1] :
                dp[i][j] = dp[i-1][j]
            else :
                sum = 0
                jj = j
                while jj > 0:
                    sum += dp[i-1][jj]
                    jj=jj-coins[i-1]
                if jj==0 :
                    sum+=1
                dp[i][j] = max(sum, dp[i-1][j])

    print(dp[N][M])
