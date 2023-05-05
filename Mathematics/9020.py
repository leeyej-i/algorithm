import sys
T=int(sys.stdin.readline())
prime = [1]*10001
result=[]
for i in range(2,10001):
    if prime[i]==0:
        continue
    else : 
        for j in range(i*2,10001,i):
            prime[j]=0
    
for _ in range(T):
    data=int(sys.stdin.readline())
    divide_num1=data//2
    divide_num2=data-divide_num1
    while prime[divide_num1]!=1 or prime[divide_num2]!=1:
        divide_num1+=1
        divide_num2-=1
    result.append([divide_num2,divide_num1])

for i in result:
    for j in i:
        print(j, end=' ')
    print()    
    