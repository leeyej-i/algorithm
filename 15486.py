# 백준 15486
# 실버 1 / 퇴사 2
import sys
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    # T = 기간 / P = 돈
    T, P = map(int, sys.stdin.readline().split())
    data.append([T, P])

dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if data[i][0] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], data[i][1] + dp[i + data[i][0]])

# print(dp)
print(dp[0])
