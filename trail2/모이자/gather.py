n = int(input())

A = list(map(int, input().split()))

m = float('inf')

for i in range(n):
    tmp = 0
    for idx, j in enumerate(A):
        tmp += abs(i - idx) * j
    m = min(m,tmp)

print(m)