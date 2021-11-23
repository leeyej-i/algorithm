import sys
T=int(sys.stdin.readline())
for _ in range(T):
    A,B=map(int, sys.stdin.readline().split())
    min_A_B = min(A,B)
    min_num=1
    for i in range(min_A_B, 1, -1):
        if A % i == 0 and B%i == 0 :
            min_num*=i
            A//=i
            B//=i
    print(min_num*A*B)
    