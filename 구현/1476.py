# 백준 1476
# 실버 5 / 날짜계산
import sys
E,S,M=map(int,sys.stdin.readline().split())
result = 0
while True:
    if E==S==M :
        result=E
        break
    else :
        min_num = min(E,S,M)
        if E == min_num :
            E+=15
        if S == min_num :
            S+=28
        if M == min_num :
            M+=19
print(result)