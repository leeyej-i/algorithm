# 백준 2446
# 브론즈 3 / 별찍기 - 9
import sys
N=int(sys.stdin.readline().strip())
n=(N-1)*2+1
for i in range(0,N):
    print(" "*i, end='')
    print("*"*n)
    n-=2
n+=4
for i in range(N-2,-1,-1):
    print(" "*i, end='')
    print("*"*n)
    n+=2
    