import sys
x,y=map(int,sys.stdin.readline().split())
small_num=min(x,y)
max_num=1
for i in range(small_num,1,-1):
    if x%i==0 and y%i==0 :
        max_num*=i
        break
min_num=max_num*(x//max_num)*(y//max_num)
print(max_num)
print(min_num)