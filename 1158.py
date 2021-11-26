# 백준 1037
# 실버 5 / 약수
import sys
N,K=map(int,sys.stdin.readline().split())
data=[i for i in range(1,N+1)]
result=[]
pop_index=K-1

while data:
    while pop_index > len(data)-1 :
        pop_index-=len(data)
    result.append(data.pop(pop_index))
    pop_index+=K-1

print("<",end='')
print(*result, sep=', ', end='')
print(">")
    