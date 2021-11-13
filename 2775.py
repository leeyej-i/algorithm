import sys
import copy
T=int(sys.stdin.readline().strip())
result=[]
for _ in range(T) :
    k=int(sys.stdin.readline().strip())
    n=int(sys.stdin.readline().strip())
    data=[i for i in range(1,n+1)]
    while k>0:
        sum=0
        for l in range(n) :
            sum+=data[l]
            data[l]=sum
        k-=1
    result.append(data[n-1])
for item in result:
    print(item)     
    