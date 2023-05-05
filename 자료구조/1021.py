# 백준 1021
# 실버 4 / 회전하는 큐
from collections import deque
import sys
N,M = map(int,sys.stdin.readline().split())
m_list = list(map(int,sys.stdin.readline().split()))
queue = deque([i for i in range(N)])

for i in range(M):
    m_list[i] = m_list[i]-1
    
result=0
for i in range(M) :
    while True :
        if queue[0] == m_list[i] :
            queue.popleft()
            break
        else :
            if queue.index(m_list[i]) < len(queue)/2 :
                while True:
                    if queue[0] == m_list[i]:
                        break
                    queue.append(queue.popleft())
                    result+=1
            else :
                while True :
                    if queue[0] == m_list[i]:
                        break
                    queue.appendleft(queue.pop())
                    result+=1
                
print(result)
        