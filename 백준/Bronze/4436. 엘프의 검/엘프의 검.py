for line in open(0):
    n = line.strip()
    x = int(n)
    s = set(n)
    t = 0
    k = 0
    while len(s) < 10:
        t += x
        k += 1
        s |= set(str(t))
    print(k)
