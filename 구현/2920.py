import sys
data=list(map(int,sys.stdin.readline().split()))
if data==sorted(data):
    print("ascending")
elif data == sorted(data, reverse=True):
    print("descending")
else :
    print("mixed")