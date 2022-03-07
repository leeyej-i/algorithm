# 백준 11055
# 실버 2 / 가장 큰 증가 부분 수열
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int,sys.stdin.readline().split()))
result = [0 for _ in range(N)]
for i in range(N):
    if i==0 :
        result[i]=A[i]
    else :
        for j in range(i):
            if A[j]<A[i]:
                result[i]=max(result[i], result[j]+A[i])
            else:
                result[i]=max(result[i], A[i])

print(max(result))