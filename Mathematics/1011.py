# 백준 1011
# 골드 5 / Fly me to the Alpha Centauri
import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    x, y = map(int,sys.stdin.readline().split())
    distanceDiff = y - x 
    sum, currentValue = 0, 1
    while True:
        if sum*2 + currentValue >= distanceDiff :
            break
        sum+= currentValue
        currentValue +=1
    result = 2*(currentValue) - 1 
    remain = distanceDiff - currentValue**2
    if remain / (currentValue) > remain // (currentValue):
        print(result +((remain//currentValue)+1)) 
    else :
        print(result +(remain//currentValue)) 