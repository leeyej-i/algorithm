# 백준 2644
# 실버 2 / 촌수계산
from collections import deque
import sys
n=int(sys.stdin.readline().strip())
a,b = map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline().strip())
array = [[0 for _ in range(n+1)] for _ in range(n+1)]
total_list = []
for _ in range(m):
    total_list.append(list(map(int,sys.stdin.readline().split())))

total_list.sort()
check=0
brother=[]
for i in range(m):
    if i == 0 :
        check = total_list[i][0]
        array[total_list[i][0]][total_list[i][1]] = array[total_list[i][1]][total_list[i][0]] = 1
        brother.append(total_list[i][1])
    else :
        if check == total_list[i][0] :
            array[total_list[i][0]][total_list[i][1]] = array[total_list[i][1]][total_list[i][0]] = 1
            brother.append(total_list[i][1])
        else :
            check = total_list[i][0]
            array[total_list[i][0]][total_list[i][1]] = array[total_list[i][1]][total_list[i][0]] = 1
            for j in range(len(brother)):
                for k in range(j+1,len(brother)):
                    array[brother[j]][brother[k]] = array[brother[k]][brother[j]]= 2
            brother.clear()

queue = deque()
queue.append([a, 0])
visit = []
while queue:
    num, result = queue.popleft()
    if num == b :
        print(result)
        exit()
    for i in range(n+1):
        if array[num][i] != 0 and i not in visit :
            queue.append([i, result+array[num][i]])
            visit.append(i)

print(-1)