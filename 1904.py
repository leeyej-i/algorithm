import sys
N=int(sys.stdin.readline())
result=[1]

for i in range(1,N+1):
    if i == 1 :
        result.append(1)
    else :
        result.append((result[i-1]+result[i-2])%15746)

print(result[N])