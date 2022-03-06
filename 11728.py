# 백준 11728  
# 실버 5 / 배열 합치기
import sys
N, M = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
C = map(str,sorted(A+B))
print(' '.join(C))