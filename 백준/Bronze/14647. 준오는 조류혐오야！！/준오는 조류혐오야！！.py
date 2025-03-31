n, m = map(int, input().split())
ls1 = [0] * n
ls2 = [0] * m

for i in range(n):
    row = input().split()
    for j, s in enumerate(row):
        c = s.count('9')
        ls1[i] += c
        ls2[j] += c

print(sum(ls1) - max(max(ls1), max(ls2)))
