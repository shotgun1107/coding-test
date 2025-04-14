_, M = map(int, input().split())
ls = list(map(int, input().split()))
print(sum(ls.index(i) >= M for i in map(int, input().split())))
