# 백준 5086
# 브론즈 3 / 배수와 약수
import sys
while(True):
    a, b = map(int, sys.stdin.readline().split())
    if a==0 and b==0 :
        break
    if a % b == 0:
        print("multiple")
    elif b % a == 0:
        print("factor")
    else :
        print("neither")
        