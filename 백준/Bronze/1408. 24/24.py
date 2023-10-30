h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t = (h2 - h1) % 24 * 3600 + (m2 - m1) * 60 + (s2 - s1)
t = (t + 24 * 3600) % (24 * 3600)

h, m = divmod(t, 3600)
m, s = divmod(m, 60)

print(f"{h:02d}:{m:02d}:{s:02d}")
