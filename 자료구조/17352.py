# 백준 17352
# 골드 5 / ABCDE

import sys


def find(x) : 
    if root[x] == x :
        return x
    return find(root[x])

def union(x,y) :
    # 각자의 루트값 찾기
    x = find(x)
    y = find(y)
    if x<y :
        root[y] = x
    else :
        root[x] = y
    
N = int(sys.stdin.readline().strip())

root = [0] * (N+1)
for i in range(N+1):
    root[i] = i
    
for _ in range(N-2):
    a, b = map(int,sys.stdin.readline().split())
    union(a,b)

res = []
for i in range(1, N+1):
    if root[i] == i :
        res.append(i)

print(res[0],res[1])
