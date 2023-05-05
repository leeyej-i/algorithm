import sys
from collections import deque
T=int(sys.stdin.readline())
result=[]
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    data=list(map(int,sys.stdin.readline().split()))
    data_array=deque()
    for i in range(len(data)):
        data_array.append([data[i],i])
        
    temp=0
    while data_array:
        max_num=max(data)
        if data_array[0][0]!=max_num:
            data_num, index = data_array.popleft()
            data_array.append([data_num, index])
        else :
            data_num, index = data_array.popleft()
            data.remove(max_num)
            temp+=1
            if index == M:
                break
    
    result.append(temp)
for item in result:
    print(item)