# 백준 2294
# 골드 5 / 동전 2
import sys

n, k = map(int,sys.stdin.readline().split())

dp = [float('inf') for _ in range(k+1)]
coin_set = set([])
for _ in range(n) :
    coin = int(sys.stdin.readline().strip())
    if coin > k :
        continue
    coin_set.add(coin)
    # 초기값 설정
    dp[coin] = 1

for i in range(1, k+1) :
    for item in coin_set :
        if i - item >= 1 :
            dp[i] = min(dp[i], dp[i-item] + 1)

if dp[k] == float('inf') :
    print(-1)
else :
    print(dp[k])