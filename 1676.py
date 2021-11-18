import sys
N=int(sys.stdin.readline().strip())

def factorial(n):
    if n==0 or n==1:
        return 1
    else :
        return n*factorial(n-1)

factorial_result=factorial(N)
result=0

while factorial_result % 10 ==0 :
    factorial_result//=10
    result+=1

print(result)