# 백준 7662
# 골드 5 / 이중 우선순위 큐
import sys
import heapq
T=int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    heap1 = []
    heap2 = []
    dictionary = dict()
    for _ in range(k):
        op, num = sys.stdin.readline().split()
        num = int(num)
        if op=='I' :
            heapq.heappush(heap1,num)
            heapq.heappush(heap2,-num)
            if num in dictionary:
                dictionary[num]+=1
            else :
                dictionary[num]=1
        elif op == 'D':
            if num == -1 :
                while heap1 :
                    pop = heapq.heappop(heap1)
                    if dictionary[pop] > 0 :
                        dictionary[pop]-=1
                        break

            else :
                while heap2 :
                    pop = (-1)*heapq.heappop(heap2)
                    if dictionary[pop] > 0 :
                        dictionary[pop]-=1
                        break
    check=-1
    while heap2 :
        pop = (-1)*heapq.heappop(heap2)
        if dictionary[pop] > 0 :
            print(pop, end=' ')
            check=1
            break
    while heap1 :
        pop = heapq.heappop(heap1)
        if dictionary[pop] > 0 :
            print(pop)
            check=1
            break
    if check == -1 :
        print("EMPTY")