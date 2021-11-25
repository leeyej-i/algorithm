import sys
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    data=[0]*(n+1)
    for i in range(1,n+1):
        if i==1:
            data[i]=1
        elif i==2:
            data[i]=2
        elif i==3:
            data[i]=4
        else:
            data[i]=data[i-1]+data[i-2]+data[i-3]
    print(data[n])