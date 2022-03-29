# 백준 2444
# 브론즈 3 / 별찍기-7
import sys
N = int(sys.stdin.readline().strip())
for n in range(N):
    for i in range(N-n-1):
        print(" ",end='')
    for j in range(2*n+1):
        print("*", end='')
    print()
for n in range(N-1):
    for i in range(n+1):
        print(" ",end='')
    for j in range(2*(N-n-1)-1) :
        print("*",end='')
    print()