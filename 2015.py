# 백준 2015
# 골드 4 / 수들의 합 4
import sys
N, K = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

sum_array = [0 for _ in range(N+1)]
for i in range(1, N+1):
    sum_array[i] = sum_array[i-1] + array[i-1]

dict = {0:1}
res = 0

for i in range(1,N+1):
    if sum_array[i]-K in dict:
        res += dict[sum_array[i]-K]
    
    if sum_array[i] in dict:
        dict[sum_array[i]] += 1
    else :
        dict[sum_array[i]] = 1

print(res)


