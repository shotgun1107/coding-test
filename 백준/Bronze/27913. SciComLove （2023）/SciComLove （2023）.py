N,Q = map(int,input().split())
s = list(("SciComLove"*(2*(10**4)))[:N])

for _ in range(Q):
    i = int(input())
    if s[i-1].isupper():
        s[i-1] = s[i-1].lower()
    else:
        s[i-1] = s[i-1].upper()
    c = 0
    for i in s:
        if i.isupper():
            c += 1
    print(c)