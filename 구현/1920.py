import sys
N=int(sys.stdin.readline())
data1=set(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
data2=list(map(int,sys.stdin.readline().split()))
for item in data2:
    if item in data1:
        print(1)
    else :
        print(0)