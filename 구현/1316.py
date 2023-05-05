import sys
N=int(sys.stdin.readline())
result=0
for _ in range(N):
    data_array=[]
    data=sys.stdin.readline().strip()
    for i in range(0,len(data)) :
        if i==0:
            data_array.append(data[i])
        else :
            if data[i]==data[i-1] :
                continue
            else :
                data_array.append(data[i])
    if len(data_array)==len(set(data_array)):
        result+=1
print(result)