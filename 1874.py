import sys
n=int(sys.stdin.readline())
stack=[]
array_data=[]
result=[]
for _ in range(n):
    array_data.append(int(sys.stdin.readline().strip()))

index=0
for i in range(1,n+1):
    stack.append(i)
    result.append('+')
    while stack:
        if stack[len(stack)-1]==array_data[index] :
            result.append('-')
            stack.pop()
            if index < n-1 :
                index+=1
            else :
                index=n-1
        else : 
            break
            
if stack :
    print("NO")
else :
    for item in result:
        print(item)
        