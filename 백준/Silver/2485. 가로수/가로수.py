import math

n = int(input())
ls = [int(input()) for _ in range(n)]

ls1 = [ls[i+1] - ls[i] for i in range(n-1)]

g = ls1[0]
for i in range(1, n-1):
    g = math.gcd(g, ls1[i])

answer = sum((i // g) - 1 for i in ls1)
print(answer)
