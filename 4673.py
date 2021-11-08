result=[0 for i in range(20000)]
for i in range(1,10001):
    next_num=i
    if i>=10000:
        next_num+=int(i/10000)
        i=i%10000
    if i>=1000:
        next_num+=int(i/1000)
        i=i%1000
    if i>=100:
        next_num+=int(i/100)
        i=i%100
    if i>=10:
        next_num+=int(i/10)
    if i>=1:
        next_num+=(i%10)
    result[next_num]=1
for k in range(1,10001):
    if(result[k]==0):
        print(k)

