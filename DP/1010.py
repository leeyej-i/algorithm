import sys
T=int(sys.stdin.readline())
result=[]
for _ in range(T) :
    N,M=map(int,sys.stdin.readline().split())
    fac_n=1
    copy_m=M
    solution=1
    for _ in range(M-N):
        solution=solution*copy_m
        copy_m=copy_m-1
    for i in range(1,M-N+1):
        fac_n=fac_n*i
    result.append(int(solution/fac_n))
for item in result:
    print(item)