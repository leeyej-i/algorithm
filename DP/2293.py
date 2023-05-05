# 백준 2293
# 골드 5 / 동전 1
import sys
n, k = map(int,sys.stdin.readline().split())
coins= []
for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))
    
dp=[0 for _ in range(k+1)]
for i in range(n):
    if coins[i] > k :
        continue
    dp[coins[i]] +=1
    for j in range(coins[i]+1, k+1):
        dp[j] += dp[j-coins[i]]
print(dp[k])