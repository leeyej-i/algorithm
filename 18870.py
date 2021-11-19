import sys
N=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data2=sorted(list(set(data)))
dictionary = {data2[i] : i for i in range(len(data2))}

for item in data:
    print(dictionary[item], end=' ')