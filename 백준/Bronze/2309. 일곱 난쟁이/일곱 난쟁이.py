from itertools import combinations

ls = [int(input()) for _ in range(9)]
comb = combinations(ls, 7)

for c in comb:
    if sum(c) == 100:
        for n in sorted(c):
            print(n)
        break