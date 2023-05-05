import sys
data=sys.stdin.readline().strip()
data_find=["c=","c-","dz=","d-","lj","nj","s=","z="]
for item in data_find:
    data=data.replace(item,"!")
print(len(data))