import sys
N=int(sys.stdin.readline())
num=N
temp=0
while 1 :
    a=int(num/10)
    b=num%10
    num=b*10+((a+b)%10)
    temp+=1
    if num==N :
        break
print(temp)
