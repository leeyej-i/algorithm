# 백준 17427
# 실버 2 / 약수의 합2
import sys
N = int(sys.stdin.readline().strip())
result = N
for i in range(2,N+1):
    result += (N//i * i)

print(result)