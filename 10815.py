# 백준 10815
# 실버 4/ 숫자 카드
import sys
N=int(sys.stdin.readline().strip())
data1=set(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline().strip())
data2=list(map(int,sys.stdin.readline().split()))

for item in data2:
    if item in data1:
        print(1, end=' ')
    else:
        print(0, end=' ')
