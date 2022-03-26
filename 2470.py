# 백준 2470
# 골드 5 / 두 용액
import sys
N = int(sys.stdin.readline().strip())
data = list(map(int,sys.stdin.readline().split()))
data.sort()

frontIndex = 0
endIndex = len(data)-1
preResult = abs(data[frontIndex] + data[endIndex])
result = preResult
resultArray = [data[frontIndex],data[endIndex]]
endIndex-=1
check = 0
while frontIndex < endIndex:
    value = abs(data[frontIndex] + data[endIndex]) 
    if value >= preResult :
        if check == 0 :
            endIndex+=1
        check = 1
        frontIndex+=1
        preResult= 2000000000
    else :
        if result > value :
            result = value
            resultArray = [data[frontIndex],data[endIndex]]
        endIndex-=1
        check = 0
        preResult = value

print("%d %d"%(resultArray[0], resultArray[1]))