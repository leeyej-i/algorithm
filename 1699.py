# 백준 1699
# 실버 3 / 제곱수의 합
import sys
N=int(sys.stdin.readline())
result=[i for i in range(N+1)]
for i in range(1,N+1):
    sub_result=[]
    for k in range(1, int(i**(1/2))+1):
        sub_result.append(result[i-k*k]+1)
    result[i]=min(sub_result)
print(result[N])