# 백준 2559
# 실버 3 / 수열
import queue
import sys
N,K=map(int,sys.stdin.readline().split())
temp = list(map(int,sys.stdin.readline().split()))

result = 0
for i in range(K):
    result+=temp[i]

sum=result
for j in range(K,N):
    sum = sum-temp[j-K]+temp[j]
    result = max(sum, result)

print(result)