import sys
N=int(sys.stdin.readline())
time_array = list(map(int, sys.stdin.readline().split()))
time_array.sort()
data=0
result=[]
for i in range(0,len(time_array)):
    data+=time_array[i]
    result.append(data)
print(sum(result))
