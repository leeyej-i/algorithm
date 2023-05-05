import sys
N=int(sys.stdin.readline())
data=[0]*10001
for _ in range(N) :
    num=int(sys.stdin.readline())
    data[num]+=1
for k in range(1,10001) :
    if data[k]==0 :
        continue
    else :
        while data[k] !=0 :
            print(k)
            data[k]-=1