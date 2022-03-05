# 백준 11052
# 실버 1 / 카드 구매하기
import sys
N=int(sys.stdin.readline())
P=list(map(int,sys.stdin.readline().split()))

result=[0 for _ in range(N+1)]
for i in range(1,N+1):
    if i == 1 :
        result[i] = P[i-1]
    else :
        result[i] = P[i-1]
        for j in range(i//2+1):
            result[i] = max(result[i-j] + result[j], result[i])

print(result[N])