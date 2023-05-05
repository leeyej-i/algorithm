# 백준 11659
# 실버 3 / 구간 합 구하기 4
import sys
N,M=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
sum_array=[0]
for i in range(1,N+1):
    if i==1:
        sum_array.append(data[i-1])
    else :
        sum_array.append(sum_array[i-1]+data[i-1])
for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print(sum_array[j]-sum_array[i-1])
