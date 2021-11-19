import sys
stair_number=int(sys.stdin.readline())
data=[0]
result=[0]
for _ in range(stair_number):
    data.append(int(sys.stdin.readline().strip()))

for i in range(1,stair_number+1):
    if i == 1:
        result.append(data[i])
    elif i == 2 :
        result.append(data[i-1]+data[i])
    else :
        result.append(max(result[i-2]+data[i],result[i-3]+data[i]+data[i-1]))
        
print(result[stair_number])