import sys
x,y,w,h=map(int,sys.stdin.readline().split())
result = min(x,y,w-x,h-y)
print(result)