# 백준 11727
# 실버 3 / 2*n 타일링 2
import sys
n=int(sys.stdin.readline())
for i in range(1,n+1):
    if i == 1:
        result=1
    elif i % 2 == 0 :
        result= result*2+1
    else :
        result= result*2-1
    result%=10007
print(result)