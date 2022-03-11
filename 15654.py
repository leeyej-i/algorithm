# 백준 15654
# 실버 3 / N과 M(5)
import sys

def func(num):
    if len(visit)==M:
        print(" ".join(map(str,visit)))
        return
    for i in range(num,N):
        if data[i] not in visit:
            visit.append(data[i])
            func(num)
            visit.pop()
N,M = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
visit=[]
func(0)