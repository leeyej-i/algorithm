import sys
from collections import Counter
N=int(sys.stdin.readline())
data=[]
for _ in range(N):
    data.append(int(sys.stdin.readline().strip()))
data.sort()
print(round(sum(data)/len(data)))
print(data[len(data)//2])

cnt = Counter(data)
cnt_max = cnt.most_common()
max_num= cnt_max[0][1]
array=[]
for item in cnt_max:
    if item[1] == max_num:
        array.append(item[0])
if len(array) > 1 :
    array.sort()
    print(array[1])
else :
    print(array[0])
    
print(max(data)-min(data))