# 백준 5585
# 브론즈 2/ 거스름돈
import sys
money=1000-int(sys.stdin.readline())
coin=[500,100,50,10,5,1]
result=0
for item in coin:
    result+=money//item
    money%=item
print(result)