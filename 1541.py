# 백준 1541
# 실버 2 / 잃어버린 괄호
import sys
import re
data=list(sys.stdin.readline().strip().split('-'))
for i in range(len(data)):
    data_item = list(map(int,data[i].split('+')))
    if i==0:
        result=sum(data_item)
    else : 
        result-=sum(data_item)

print(result)