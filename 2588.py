import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
result=[]
result.append(a*(b%10))
result.append(a*(int(b/10)%10))
result.append(a*int(b/100))
result.append(result[0]+result[1]*10+result[2]*100)
for item in result:
    print(item)
