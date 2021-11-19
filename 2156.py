import sys
n=int(sys.stdin.readline())
data=[0]
result=[0]
for _ in range(n):
    data.append(int(sys.stdin.readline()))
for i in range(1,n+1):
    if i ==1 :
        result.append(data[i])
    elif i==2 :
        result.append(data[i-1]+data[i])
    else :
        result.append(max(result[i-1],result[i-2]+data[i],result[i-3]+data[i]+data[i-1]))

print(result[n])
        