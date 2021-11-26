# 백준 13305
# 실버 4 / 주유소
import sys
N=int(sys.stdin.readline())
distance=list(map(int,sys.stdin.readline().split()))
oil_price=list(map(int,sys.stdin.readline().split()))
for i in range(N-1):
    if i==0:
        result=distance[i]*oil_price[i]
    else :
        result=result+distance[i]*min(oil_price[i], oil_price[i-1])

print(result)
