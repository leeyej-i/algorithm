import sys
result=[]
while 1 :
    try :
        A,B=map(int,sys.stdin.readline().split())
        result.append(A+B)
    except:
        break
for item in result :
    print(item)