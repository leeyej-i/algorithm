import sys
data1=[]
data2=[]
for _ in range(3):
    x,y=map(int,sys.stdin.readline().split())
    data1.append(x)
    data2.append(y)
for item in data1:
    if data1.count(item)==1:
        result1=item
for item in data2:
    if data2.count(item)==1:
        result2=item
print(result1,result2)   