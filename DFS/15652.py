# 백준 15652
# 실버 3 / N과 M(4)
import sys
N,M=map(int,sys.stdin.readline().split())
data=[i for i in range(1,N+1)]
visit=[]
def array_function(num) :
    if len(visit)==M:
        print(' '.join(map(str,visit)))
        return
    for i in range(num,N) :
        visit.append(data[i])
        array_function(i)
        visit.pop()
array_function(0)