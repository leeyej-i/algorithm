import sys
data=[]
for _ in range(9):
    data.append(int(sys.stdin.readline().strip()))
sum = sum(data)-100

def resolve() :
    for i in range(8):
        for k in range(i+1,9):
            if data[i]+data[k]==sum :
                data.remove(data[k])
                data.remove(data[i])
                return
    
resolve()
data.sort()
for item in data:
    print(item)
