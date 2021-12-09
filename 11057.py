# 백준 11057
# 실버 1 / 오르막 수
import sys
N=int(sys.stdin.readline().strip())
for i in range(1,N+1):
    if i == 1 :
        result = 10
    else :
        result=result*(9+i)//i
print(result%10007)