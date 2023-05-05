# 백준 1946
# 실버 1 / 신입사원
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    data=[]
    for _ in range(N):
        data.append(list(map(int,sys.stdin.readline().split())))
    data.sort()
    first_rank=data[0][1]
    result=1
    for i in range(1, N):
        if first_rank < data[i][1] :
            continue
        else :
            result+=1
            first_rank=data[i][1]
    print(result)