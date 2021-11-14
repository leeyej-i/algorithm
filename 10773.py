import sys
K=int(sys.stdin.readline().strip())
data=[]
for _ in range(K):
    num=int(sys.stdin.readline().strip())
    if num == 0 :
        data.pop()
    else :
        data.append(num)
print(sum(data))