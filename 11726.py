import sys
n=int(sys.stdin.readline().strip())
data=[1,2]
for i in range(2,n):
    data.append(data[i-2]+data[i-1])
print(data[n-1]%10007)