# 백준 2635
# 실버 5/ 수 이어가기
import sys
N=int(sys.stdin.readline().strip())
result_array = []
cnt = 1

for i in range(1,N+1):
    N2=N
    array = [N]
    array.append(i)
    j=1
    while True: 
        if array[j-1]-array[j] < 0:
            break 
        array.append(array[j-1]-array[j])
        j+=1
        
    if len(array)>cnt:
        cnt = len(array)
        result_array=array

print(cnt)
for item in result_array:
    print(item, end=' ')