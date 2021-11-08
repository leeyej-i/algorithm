import sys
H,M=map(int,sys.stdin.readline().split())
if M>=45 :
    print(H,(M-45), sep=" ")
else :
    if H != 0 :
        print((H-1),(M+15), sep=" ")
    else :
        print((H+23),(M+15), sep=" ")