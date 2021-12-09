# 백준 1292
# 실버 5 / 쉽게 푸는 문제
import sys
A,B=map(int,sys.stdin.readline().split())
data=[0]
def solve(num):
    temp=1
    result=0
    while True :
        for _ in range(temp):
            result+=temp
            num-=1
            data.append(result)
            if num==0 :
                return
        temp+=1
solve(B)
print(data[B]-data[A-1])