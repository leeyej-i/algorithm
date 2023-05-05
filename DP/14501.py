# 백준 14501
# 실버 3 / 퇴사
import sys
N = int(sys.stdin.readline().strip())
times =[0 for _ in range(N+1)]
pays=[0 for _ in range(N+1)]
for i in range(1,N+1):
    t, p = map(int,sys.stdin.readline().split())
    times[i], pays[i] = t, p

dp=[0 for _ in range(N+2)]
for i in range(N, 0, -1):
    if times[i] + i -1 > N :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1], pays[i]+dp[i+times[i]])
    
print(dp[1])