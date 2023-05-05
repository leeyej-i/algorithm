import sys
T=int(sys.stdin.readline())
data=[]
for _ in range(T):
    data.append(int(sys.stdin.readline().strip()))
max_data=max(data)
array_data=[0]*(max_data+1)

for i in range(1,max_data+1):
    if i==1 or i==2 or i==3:
        array_data[i]=1
    else :
        array_data[i]=array_data[i-2]+array_data[i-3]

for item in data:
    print(array_data[item])    
    