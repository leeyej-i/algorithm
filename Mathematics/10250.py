import sys
T=int(sys.stdin.readline())
result=[0]*2*T
for i in range(0,T*2,2) :
    H,W,N=map(int,sys.stdin.readline().split())
    while(N>H):
        N-=H
        result[i+1]+=1
    result[i]+=N
    result[i+1]+=1
for k in range(0,len(result),2) :
    print(result[k],end='')
    print("%02d" %result[k+1])
        