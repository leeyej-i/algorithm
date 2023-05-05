import sys
M=int(sys.stdin.readline().strip())
N=int(sys.stdin.readline().strip())
data=[]
for i in range(M, N+1) :
    if i == 1 :
        continue
    check_number = 0
    for k in range(2, int(i**0.5)+1):
        if i % k == 0 :
            check_number +=1
            break
    if check_number == 0:
        data.append(i)
if len(data)==0 :
    print(-1)
else :
    print(sum(data))
    print(min(data))
        