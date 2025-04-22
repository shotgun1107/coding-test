N = int(input())
best_sum, best_base = 0, 2

for b in range(2, N + 1):
    x, s = N, 0
    while x:
        s += x % b
        x //= b
    if s > best_sum:
        best_sum, best_base = s, b

print(best_sum, best_base)
