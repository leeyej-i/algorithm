# 백준 15650
# 실버 3 / N과 M(2)
import sys
N,M=map(int,sys.stdin.readline().split())
data=[i for i in range(1,N+1)]
temp=0
visit=[]
def array_function(num) :
    if len(visit)==M:
        print(' '.join(map(str,visit)))
        return
    for i in range(num,N) :
        if data[i] not in visit:
            visit.append(data[i])
            array_function(i+1)
            visit.pop()
array_function(0)