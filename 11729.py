# 백준 11729
# 실버 1 / 하노이 탑 이동 순서
import sys

def func(n, first, second, third):
    global res
    if n == 1 :
        result.append([first, third])
        res+=1
        return
    func(n-1, first, third, second)
    result.append([first, third])
    res+=1
    func(n-1, second, first, third)

K = int(sys.stdin.readline().strip())
res = 0
result = []
func(K,1,2,3)
print(res)
for item in result:
    print(item[0], item[1])