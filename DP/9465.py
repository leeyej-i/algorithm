# 백준 9465
# 실버 1 / 스티커
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    data=[]
    for _ in range(2):
        data.append(list(map(int,sys.stdin.readline().split())))
    
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for j in range(n):
        for i in range(2):
            if j==0 :
                dp[i][j] = data[i][j]
            else :
                if i==0:
                    dp[i][j] = max(dp[1][j-1]+data[i][j],dp[0][j-1]-data[0][j-1]+data[i][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[0][j-1]+data[i][j],dp[1][j-1]-data[1][j-1]+data[i][j], dp[i][j-1])
    print(max(dp[0][n-1], dp[1][n-1]))