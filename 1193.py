import sys
X=int(sys.stdin.readline())
temp=0
i=1
while X>0:
    X-=i
    temp+=1
    i+=1
if temp%2==0:
    fist_num=1
    second_num=i-1
    for i in range(-1*(temp-1),X):
        fist_num+=1
        second_num-=1
else :
    fist_num=i-1
    second_num=1
    for i in range(-1*(temp-1),X):
        fist_num-=1
        second_num+=1
print(str(fist_num)+"/"+str(second_num))
