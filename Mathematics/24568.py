# 백준 24568
# 브론즈 5 / Cupcake Party
import sys
R = int(sys.stdin.readline().strip())
S = int(sys.stdin.readline().strip())

result = R*8 + S*3 - 28

if result < 0 :
    print(0)
else :
    print(result)