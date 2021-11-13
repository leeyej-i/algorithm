from collections import deque
import sys
N=int(sys.stdin.readline())
data_deque=deque([i for i in range(1,N+1)])

while len(data_deque)>1:
    data_deque.popleft()
    first_num=data_deque.popleft()
    data_deque.append(first_num)
    
print(data_deque[0])