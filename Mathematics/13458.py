# 백준 13458
# 브론즈 2 / 시험감독
import sys
N=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))
B,C=map(int,sys.stdin.readline().split())

result = N
for item in array :
    num = item - B 
    if num > 0 :
        if num - (num // C)*C > 0:
            result+=(num//C)+1
        else :
            result+=num//C

print(result)