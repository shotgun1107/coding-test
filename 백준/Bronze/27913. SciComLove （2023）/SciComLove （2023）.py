N, Q = map(int, input().split())

base = "SciComLove"
s = list((base * (N // len(base) + 1))[:N])

c = sum(1 for c in s if c.isupper())

for _ in range(Q):
    i = int(input())
    i -= 1

    if s[i].isupper():
        c -= 1
        s[i] = s[i].lower()
    else:
        c += 1
        s[i] = s[i].upper()
    print(c)