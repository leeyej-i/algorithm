# 백준 1964
# 브론즈 3 / 오각형, 오각형, 오각형...
import sys
N=int(sys.stdin.readline())
result=0
increase=0
for i in range(N):
    if i==0 :
        result = 5
        increase = 7
    else :
        result+=increase
        increase+=3
print(result%45678)
