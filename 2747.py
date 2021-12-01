# 백준 2747
# 브론즈 3 / 피보나치수
import sys
n=int(sys.stdin.readline())
data=[0,1]
for i in range(2,n+1):
    data.append(data[i-1]+data[i-2])

print(data[n])