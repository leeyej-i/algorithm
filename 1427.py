import sys
num=str(sys.stdin.readline().strip())
data=list(num)
data.sort(reverse=True)
for item in data:
    print(item, end='')
