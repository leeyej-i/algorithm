# 백준 15651
# 실버 3 / N과 M(3)
import sys
N,M=map(int,sys.stdin.readline().split())
data=[i for i in range(1,N+1)]
temp=0
visit=[]
def array_function() :
    if len(visit)==M:
        print(' '.join(map(str,visit)))
        return
    for i in range(N) :
        visit.append(data[i])
        array_function()
        visit.pop()
array_function()