# 백준 1475
# 실버 5 / 방 번호
import sys
data=list(sys.stdin.readline().strip())
result=[0]*9
for item in data :
    for i in range(9):
        if int(item)==i:
            result[i]+=1
            break
        elif int(item)==9:
            result[6]+=1
            break
if result[6] % 2 == 0:
    result[6]//=2
else :
    result[6]=result[6]//2 +1
print(max(result))