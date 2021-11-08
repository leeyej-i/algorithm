import sys
data=[]
for _ in range(9):
    data.append(int(sys.stdin.readline()))
max=max(data)
print(max)
for i in range(9):
    if(data[i]==max):
        print(i+1)