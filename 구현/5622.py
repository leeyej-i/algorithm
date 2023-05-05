import sys
data= sys.stdin.readline().strip()
result=0
for i in range(len(data)) :
    time=0
    number=0
    if data[i]=='A' or data[i]=='B' or data[i]=='C':
        number=2
    elif data[i]=='D' or data[i]=='E' or data[i]=='F':
        number=3
    elif data[i]=='G' or data[i]=='H' or data[i]=='I':
        number=4
    elif data[i]=='J' or data[i]=='K' or data[i]=='L':
        number=5
    elif data[i]=='M' or data[i]=='N' or data[i]=='O':
        number=6
    elif data[i]=='P' or data[i]=='Q' or data[i]=='R' or data[i]=='S':
        number=7
    elif data[i]=='T' or data[i]=='U' or data[i]=='V':
        number=8
    elif data[i]=='W' or data[i]=='X' or data[i]=='Y' or data[i]=='Z':
        number=9
    time=number+1
    result+=time
print(result)