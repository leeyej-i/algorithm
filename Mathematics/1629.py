# 백준 1912
# 실버 1 / 곱셈
import sys
A,B,C=map(int,sys.stdin.readline().split())

def solve(a,b) :
    if b==1:
        return a%C
    else :
        result=solve(a,b//2)
        if b%2==0:
            return result * result % C
        else :
            return a * result * result %C

print(solve(A,B))