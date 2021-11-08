num = input()
num = int(num)
for i in range(0, num) :
    x1,y1,x2,y2=map(int,input().split())
    p_num = input()
    p_num = int(p_num)
    cx=[] #각 배열 개수는 p_num
    cy=[]
    r=[]
    for k in range(0, p_num) :
        a,b,c = map(int,input().split())
        cx.append(a)
        cy.append(b)
        r.append(c)
    
    
