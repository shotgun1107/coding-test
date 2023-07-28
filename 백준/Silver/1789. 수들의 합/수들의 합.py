n = int(input())
n1 = 1
n2 = n
c = 0
while True:
    if n - n1 < 0:
        print(c)
        break
    n -= n1
    n1 += 1
    c += 1