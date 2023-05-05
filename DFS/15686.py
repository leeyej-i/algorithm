# 백준 15686
# 골드 5 / 치킨 배달
from copy import deepcopy
from itertools import combinations
import sys
                        
N,M=map(int,sys.stdin.readline().split())
data = []
for _ in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))
    
homes = []
stores = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            homes.append([i,j])
        elif data[i][j] == 2:
            stores.append([i,j])

comb = list(combinations(stores,M))
result = 0
for i in comb :
    comb_result = 0
    for j in homes :
        sum = 0
        for l in i :
            if sum == 0 :
                sum = abs(j[0]-l[0]) + abs(j[1]-l[1])
            else :
                sum = min(sum, abs(j[0]-l[0]) + abs(j[1]-l[1]))
        comb_result +=sum
    if result == 0 :
        result = comb_result
    else :
        result = min(result, comb_result)
print(result)