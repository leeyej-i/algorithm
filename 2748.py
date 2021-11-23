import sys
n=int(sys.stdin.readline())
data=[0,1]
if n==1 :
    print(1)
else : 
    for i in range(2,n+1):
        data.append(data[i-1]+data[i-2])
    print(data[len(data)-1])