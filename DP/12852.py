# 백준 12852
# 실버 1/ 1로 만들기 2
import sys
N = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(N+1)]
for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = i-1
    if i % 3 == 0:
        if dp[i][0] > dp[i//3][0] + 1:
            dp[i][0] = dp[i//3][0] + 1
            dp[i][1] = i//3
    if i % 2 == 0:
        if dp[i][0] > dp[i//2][0] + 1:
            dp[i][0] = dp[i//2][0] + 1
            dp[i][1] = i//2

print(dp[N][0])
print(N, end=' ')
if N != 1:
    result = dp[N][1]
    while True:
        print(result, end=' ')
        result = dp[result][1]
        if result == 0:
            break
