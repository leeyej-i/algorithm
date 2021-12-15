# 백준 11718
# 브론즈 3/ 그대로 출력하기
import sys
temp=0
while True:
    if temp == 100 :
        break
    data=sys.stdin.readline().strip()
    print(data)
    temp+=1