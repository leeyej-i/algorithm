# 백준 1759
# 골드 5 / 암호 만들기
from copy import deepcopy
import sys

def back(cnt, num):
    if cnt == L :
        visit2 = deepcopy(visit)
        result.append(visit2)
        return
    for i in range(num, C):
        if data[i] not in visit:
            visit.append(data[i])
            back(cnt+1, i)
            visit.pop()

L,C = map(int,sys.stdin.readline().split())
data = list(sys.stdin.readline().split())
data.sort()
visit=[]
result =[]
back(0,0)
for x in result:
    m, j = 0,0
    for y in x :
        if y in ['a', 'e', 'i', 'o', 'u']:
            m+=1
        else :
            j+=1
    if m >= 1 and j >= 2:
        print("".join(x))
