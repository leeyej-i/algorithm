import sys
N,M=map(int, sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
result=0
for i in range(N):
    for k in range(i+1,N):
        for j in range(k+1,N):
            if data[i]+data[k]+data[j]<=M:
                if result>data[i]+data[k]+data[j]:
                    continue
                else :
                    result=data[i]+data[k]+data[j]
            else :
                continue
print(result)
            