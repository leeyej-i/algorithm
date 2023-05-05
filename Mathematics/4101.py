# 백준 4101
# 브론즈 3 / 크냐?
import sys
while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0 :
        break
    elif a > b:
        print("Yes")
    else :
        print("No")