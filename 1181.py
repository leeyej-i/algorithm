import sys
N=int(sys.stdin.readline().strip())
data=[]
for _ in range(N) :
    word=str(sys.stdin.readline().strip())
    data.append(word)
data=list(set(data))
data.sort()
data.sort(key=len)
for item in data:
    print(item)