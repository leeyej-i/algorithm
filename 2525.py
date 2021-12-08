# 백준 2525
# 브론즈 4 / 오븐 시계
import sys
A,B=map(int,sys.stdin.readline().split())
C=int(sys.stdin.readline().strip())
B+=C 
A+=(B//60)
B%=60
A%=24
print("%d %d" %(A,B))