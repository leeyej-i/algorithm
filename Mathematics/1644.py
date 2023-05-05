# 백준 1644
# 골드 3 / 소수의 연속합

prime = [1]*4000000
result = []
for i in range(2, 10001):
    if prime[i] == 0:
        continue
    else:
        for j in range(i*2, 10001, i):
            prime[j] = 0
