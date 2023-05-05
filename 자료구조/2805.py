import sys
N, M =map(int,sys.stdin.readline().split())
tree_length=list(map(int, sys.stdin.readline().split()))
min, max= 1, max(tree_length)
while min<=max :
    middle = (min+max)//2
    data=sum([item-middle for item in tree_length if middle<item])
    if data >= M :
        min= middle+1
    else :
        max=middle-1
print(min-1)