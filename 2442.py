import sys
N=int(sys.stdin.readline())
for i in range(1,N+1):
    print(" "*(N-i),end='')
    print("*"*(i*2-1))