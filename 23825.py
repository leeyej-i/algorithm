# 백준 23825
# 브론즈 4 / SASA 모형을 만들어보자
import sys
N,M=map(int,sys.stdin.readline().split())
min_num=min(N,M)
print(min_num//2)
