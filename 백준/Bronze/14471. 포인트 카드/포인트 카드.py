N, M = map(int, input().split())
full, ls = 0, []
for _ in range(M):
    a, _ = map(int, input().split())
    if a >= N:
        full += 1
    else:
        ls.append(a)
ls.sort(reverse=True)
print(sum(N - a for a in ls[:max(0, len(ls)-1)]))