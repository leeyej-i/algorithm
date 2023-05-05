import sys
data=[]
for _ in range(10):
    n=int(sys.stdin.readline())
    data.append(n%42)
data_set=list(set(data))
print(len(data_set))