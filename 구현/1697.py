import sys
N,K=map(int,sys.stdin.readline().split())

def solve(n,k):
    if n < k :
        if k==1 :
            return 1
        elif k%2 == 1:
            return min(solve(n,k+1)+1,solve(n,k-1)+1)
        else : 
            return min(solve(n,k//2)+1,k-n)
    else :
        return n-k
    
print(solve(N,K))