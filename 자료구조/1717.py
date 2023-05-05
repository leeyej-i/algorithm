# 백준 1717
# 골드 4 / 집합의 표현
import sys


def find(node):
    if setList[node] == node:
        return node
    else:
        return find(setList[node])


n, m = map(int, sys.stdin.readline().split())
setList = [i for i in range(n+1)]
for _ in range(m):
    calc, a, b = map(int, sys.stdin.readline().split())
    if calc == 0:
        findA = find(a)
        findB = find(b)
        if findA < findB:
            setList[findB] = findA
        else:
            setList[findA] = findB
    else:
        if a == b:
            print("YES")
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
