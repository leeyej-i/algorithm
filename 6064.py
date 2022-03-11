# 백준 6064
# 실버 1 / 카잉 달력
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    result=x
    if N == y :
        y-=N
    while result % N != y :
        result += M
        if (result - x) % N == 0 :
            result=-1
            break
    print(result)
        