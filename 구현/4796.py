# 백준 4796
# 실버 5 / 캠핑
import sys
cnt=0
while True:
    cnt+=1
    L, P, V = map(int,sys.stdin.readline().split())
    if L==P==V==0 : break
    result = 0
    result += (V//P)*L 
    if V%P <= L :
        result += V%P
    else :
        result += L
    print("Case %d: %d" %(cnt, result))