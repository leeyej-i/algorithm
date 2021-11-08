import sys
A,B,V=map(int,sys.stdin.readline().split())
day=(V-B)/(A-B)
if day!=int(day):
    day+=1
day=int(day)
print(day)