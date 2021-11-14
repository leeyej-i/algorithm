import sys
N=int(sys.stdin.readline().strip())
result=0
for i in range(N-1,0,-1):
    num=i
    divide_sum=i
    while num // 10 > 0 :
        divide_sum+=num%10
        num=num//10
    divide_sum+=num
    if divide_sum==N:
        result=i       
print(result)