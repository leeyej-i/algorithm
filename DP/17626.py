# 백준 17626
# 실버 4 / Four Squares
import sys

n = int(sys.stdin.readline())
dp=[0 for _ in range(n+1)]
squared = [] 
for i in range(1,int(n**(1/2))+1):
    dp[i**2] = 1
    squared.append(i**2)

for i in range(1, n+1):
    if dp[i] == 0 :
        dp[i] = dp[i-1]+1
        k=0
        for item in squared :
            if item < i :
                dp[i] = min(dp[i], dp[i-item]+1)
        
print(dp[n])