import sys
from collections import Counter
data=sys.stdin.readline().rstrip()
data=data.upper()
count=Counter(data)
desc=count.most_common()
if len(data)!=1 :
    if desc[0][1]==desc[1][1] :
        print("?")
    else :
        print(desc[0][0])
else :
    print(data)

