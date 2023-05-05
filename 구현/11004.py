# 백준 11004
# 실버 5 / K번째  수
import sys
N,K=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
data.sort()
print(data[K-1])
