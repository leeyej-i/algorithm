# 백준 1765
# 골드 2 / 닭싸움 팀 정하기
import sys


def find(x):
    if root[x] == x:
        return x
    return find(root[x])


def union(x, y):
    # 각자의 루트값 찾기
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y


# 학생의 수
n = int(sys.stdin.readline().strip())
# 인간관계 수
m = int(sys.stdin.readline().strip())
relation = [[0 for _ in range(n+1)] for _ in range(n+1)]


# 인간관계 리스트 정리
for _ in range(m):
    r, p, q = sys.stdin.readline().split()
    p, q = int(p), int(q)
    if r == 'F':
        relation[p][q] = relation[q][p] = 1
    else:
        relation[p][q] = relation[q][p] = -1

# 원수의 원수는 친구
for i in range(1, n+1):
    e_list = []
    for j in range(1, n+1):
        if relation[i][j] == -1:
            e_list.append(j)
    for k in range(len(e_list)):
        for l in range(k+1, len(e_list)):
            relation[e_list[k]][e_list[l]] = relation[e_list[l]][e_list[k]] = 1

# 모든 사람들을 각각 그룹으로 만듦
root = [0] * (n+1)
for i in range(n+1):
    root[i] = i

# 친구끼리는 결합
for i in range(1, n+1):
    for j in range(1, n+1):
        if relation[i][j] == 1:
            union(i, j)

# 루트가 자신인 수(그룹 수) 체크
res = 0
for i in range(1, n+1):
    if root[i] == i:
        res += 1

print(res)
