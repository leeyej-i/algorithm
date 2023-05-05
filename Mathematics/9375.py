# 백준 9375
# 실버 3 / 패션왕 신해빈
import sys
T=int(sys.stdin.readline().strip())
for _ in range(T):
    dic=dict()
    n=int(sys.stdin.readline().strip())
    for _ in range(n):
        name, kind = sys.stdin.readline().split()
        if kind in dic :
            dic[kind].append(name)
        else :
            dic[kind]=[name]
    result=1
    for item in dic:
        result*=(len(dic[item])+1)
    print(result-1)