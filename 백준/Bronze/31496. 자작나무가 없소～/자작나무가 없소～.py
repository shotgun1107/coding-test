N, S = input().split()
print(sum(int(c) for s, c in (input().split() for _ in range(int(N))) if S in s.split('_')))
