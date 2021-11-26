# 백준 1158
# 실버 5 / 요세푸스 문제
import sys
N=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
if len(data)==1:
    result=data[0]*data[0]
else : 
    result=max(data)*min(data)
print(result)