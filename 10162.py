# 백준 10162
# 브론즈 4 / 전자레인지
import sys
T=int(sys.stdin.readline())
a,b,c=0,0,0
a=T//300
T=T%300
b=T//60
T=T%60
c=T//10
if T%10 !=0 :
    print(-1)
else :
    print("%d %d %d" %(a,b,c))
