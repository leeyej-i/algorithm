import sys
result_array=[]
while 1:
    x,y,z=map(int,sys.stdin.readline().split())
    if x==0 and y==0 and z==0 :
        break
    if x == max(x,y,z) :
        x,z = z,x
    elif y == max(x,y,z) :
        y,z = z,y
    if z**2==x**2+y**2:
        result = 'right'
    else :
        result = 'wrong'
    result_array.append(result)
for item in result_array : 
    print(item)