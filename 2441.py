# 백준 2441
# 브론즈 3 / 별 찍기 _ 4
import sys
N=int(sys.stdin.readline())
for i in range(N):
    print(" "*i,end='')
    print("*"*(N-i),end='')
    print()