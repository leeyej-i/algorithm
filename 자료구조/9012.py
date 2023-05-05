from os import close
import sys
T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    data=sys.stdin.readline().strip()
    open_string=0
    close_string=0
    for i in range(len(data)):
        if data[i]=='(':
            open_string+=1
        else :
            close_string+=1
        if close_string > open_string :
            break
    if open_string == close_string:
        result.append("YES")
    else :
        result.append("NO")
for item in result:
    print(item) 