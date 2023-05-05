import sys
T=int(sys.stdin.readline())
result=[]
for _ in range(T) :
    R,S = sys.stdin.readline().split()
    S.strip()
    R=int(R)
    for i in range(0,len(S)) :
        data=S[i]*R
        result.append(data)
    result.append("-1")
for item in result:
    if(item=='-1'):
        print("")
        continue
    print(item, end="")