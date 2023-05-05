import sys
N=int(sys.stdin.readline())
num=N-1
for _ in range(N) :
    for _ in range(0,N-num):
        print("*",end='')
    num-=1
    print("")