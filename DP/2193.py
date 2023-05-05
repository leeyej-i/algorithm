# 백준 2193
# 실버 3 / 이친수
import sys
N=int(sys.stdin.readline())
data=[0]*(N+1)
for i in range(1,N+1):
    if i==1 or i==2:
        data[i] = 1
    else :
        data[i]=data[i-1]+data[i-2]

print(data[N])