import sys
N=int(sys.stdin.readline())
data=[]
result=[]
for _ in range(N) :
    order = sys.stdin.readline().strip()
    if order.find("push")>-1 :
        order, num = order.split()
        data.append(num)
    elif order.find("top")>-1 :
        if len(data)==0:
            result.append(-1)
        else :
            result.append(data[len(data)-1])
    elif order.find("size")>-1 :
        result.append(len(data))
    elif order.find("empty")>-1 :
        if len(data)==0 :
            result.append(1)
        else :
            result.append(0)
    elif order.find("pop") > -1 :
        if len(data)==0:
            result.append(-1)
        else :
            result.append(data[len(data)-1])
            data.pop(len(data)-1)
for item in result :
    print(item)