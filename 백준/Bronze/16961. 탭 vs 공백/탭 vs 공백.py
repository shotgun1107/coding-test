from collections import Counter

T = []
S = []
k = 0
for _ in range(int(input())):
    c,s,e = input().split()
    s , e = int(s), int(e)
    k = max(k,e-s)
    if c == 'T':
        T.append([i for i in range(s,e+1)])
    else:
        S.append([i for i in range(s,e+1)])

T_c = Counter(sum(T,[]))
S_c = Counter(sum(S,[]))

c = 0
l = 0
for day in set(T_c) & set(S_c):
    if T_c[day] == S_c[day]:
        c += 1
        l = max(l, T_c[day] + S_c[day])
print(len(set(sum(T,[])) | set(sum(S,[]))))
print(max(Counter(sum(T,[]) + sum(S ,[])).values()))
print(c)
print(l)
print(k+1)