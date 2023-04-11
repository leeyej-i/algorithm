# 백준 14926
# 실버 5 / 거스름 돈
import sys
n = int(sys.stdin.readline().strip())

dp = [float('inf') for _ in range(n+1)]
for i in range(1, n+1):
    if i == 2 or i == 5 :
        dp[i] = 1
        continue
    if i-2 >= 0 and dp[i-2] != float('inf') :
        dp[i] = min(dp[i], dp[i-2] + 1)
    if i-5 >= 0 and dp[i-5] != float('inf') :
        dp[i] = min(dp[i], dp[i-5] + 1)
if dp[n] == float('inf'):
    print(-1)
    exit()
print(dp[n])