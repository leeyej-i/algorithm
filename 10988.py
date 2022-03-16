# 백준 10988
# 브론즈 1 / 팰린드롬인지 확인하기
import sys
data = sys.stdin.readline().strip()
i, j = 0, len(data)-1
while i <= j :
    if data[i] == data[j] :
        i+=1
        j-=1
    else :
        print(0)
        exit()
print(1)