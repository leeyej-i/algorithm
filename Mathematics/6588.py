# 백준 6588
# 실버 1 / 골드바흐의 추측
import sys
prime = [1]*1000001
result=[]
for i in range(2,1000000):
    if prime[i]==0:
        continue
    else : 
        for j in range(i*2,1000000,i):
            prime[j]=0

while True:
    n=int(sys.stdin.readline())
    result=0
    if n == 0:
        break
    for i in range(3, n//2+1,2):
        if prime[i]==1 and prime[n-i]==1:
            result=i
            break
    if result==0:
        print("Goldbach's conjecture is wrong.")
    else :
        a= result
        b= n-result
        print("%d = %d + %d" %(n, a, b))