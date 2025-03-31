s = open(0).read().split('\n')
s.pop()
for i in s:
    a,b,c,d = 0, 0, 0, 0
    for j in i:
        j = str(j)
        if j.islower():
            a += 1
        elif j.isupper():
            b += 1
        elif j == ' ':
            d += 1
        else:
            c += 1
    print(a,b,c,d)