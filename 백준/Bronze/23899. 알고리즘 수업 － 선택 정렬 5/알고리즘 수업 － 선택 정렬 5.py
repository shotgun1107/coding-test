n = int(input())
ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if ls1 == ls2:
        break
    idx = ls1.index(max(ls1[:i + 1]))
    if idx != i:
        ls1[idx], ls1[i] = ls1[i], ls1[idx]

print(1 if ls1 == ls2 else 0)