import sys
data=list(map(int,sys.stdin.readline().split()))
sum=0
for item in data:
    sum+=item**2
print(sum%10)