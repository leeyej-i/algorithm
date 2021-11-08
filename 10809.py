import sys
result=[-1 for i in range(26)]
data=sys.stdin.readline().strip()
for i in range(len(data)):
    if(result[ord(data[i])-97]==-1):
        result[ord(data[i])-97]=i
for item in result:
    print(item,end=" ")