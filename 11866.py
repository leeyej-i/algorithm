import sys
N,K=map(int,sys.stdin.readline().split())
data=[i for i in range(1,N+1)]
result=[]
pop_num=0
while data :
    pop_num+=(K-1)
    while pop_num>len(data)-1 :
        pop_num=pop_num-len(data)
    result.append(data.pop(pop_num))
print("<",end='')
print(*result,sep=', ',end='')
print(">")

    