# 백준 11051
# 실버 1 / 이항 계수 2
import sys
N, K = map(int,sys.stdin.readline().split())
result = 1
n = N
for i in range(K) :
    result *= n
    n-=1

subResult = 1
for i in range(1, K+1):
    subResult *= i

result //= subResult
print(result%10007)