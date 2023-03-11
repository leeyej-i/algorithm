# 백준 15990
# 실버 2 / 1,2,3 더하기 5
import sys

T = int(sys.stdin.readline().strip())

dp = [[0,0,0] for _ in range(100001)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4,100001) :
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for _ in range(T):
    item = int(sys.stdin.readline().strip())
    print((dp[item][0] + dp[item][1] + dp[item][2]) % 1000000009)
