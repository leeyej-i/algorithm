import sys
A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
C=int(sys.stdin.readline())
result=[0 for _ in range(10)]
data=A*B*C
while 1 :
    if(data==0):
        break
    result[data%10]+=1
    data=int(data/10)
for item in result:
    print(item)    