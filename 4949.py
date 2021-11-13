import sys
result_array=[]
while 1:
    data=sys.stdin.readline().rstrip()
    data_array=[]
    result=1
    if data=='.':
        break
    
    for i in range(len(data)):
        if data[i]=='(' or data[i]=='[' :
            data_array.append(data[i])
            continue
        elif data[i]==')':
            if len(data_array)==0:
                result=0
                break
            else :
                if data_array.pop()=='(':
                    continue
                else :
                    result=0
                    break
        elif data[i]==']':
            if len(data_array)==0:
                result=0
                break
            else :
                if data_array.pop()=='[':
                    continue
                else : 
                    result=0
                    break
    if result== 1:
        if len(data_array)==0:
            result_array.append(result)
        else :
            result=0
            result_array.append(result)
    else :
        result_array.append(result)
    
for item in result_array:
    if item==1 :
        print("yes")
    else :
        print("no")