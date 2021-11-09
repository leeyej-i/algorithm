import sys
n=int(sys.stdin.readline())
first_num=0
second_num=1
result=0
for i in range(n+1):
    if i==0 :
        result=first_num
    elif i==1 :
        result=second_num
    else :
        result=first_num+second_num
        first_num=second_num
        second_num=result
print(result)