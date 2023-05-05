# 백준 2914
# 브론즈 5 / 저작권
import sys
A, I =map(int,sys.stdin.readline().split())
if A == 1:
    print(A*I)
else :
    print(A*(I-1)+1)