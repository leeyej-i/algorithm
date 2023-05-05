import sys
N=int(sys.stdin.readline())
data_array=[]
for _ in range(N):
    data=list(map(int,sys.stdin.readline().split()))
    data_array.append(data)
data_array.sort(key=lambda x : (x[1],x[0]))
time=0
count=0
for i in range(N):
    if data_array[i][0]>=time :
       time = data_array[i][1]
       count+=1
print(count) 