from math import ceil

for _ in range(int(input())):
    S = input()
    S_ = S[:ceil(len(S) / 3)]
    r = S_[::-1]
    t = S_[1:]
    print(1 if S in (S_+r+S_, S_+r[1:]+S_, S_+r+t, S_+r[1:]+t) else 0)
