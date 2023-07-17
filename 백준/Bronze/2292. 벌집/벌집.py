ls = [0,1]

i = 1

while True:
    ls.append(int(ls[i] + (6*i)))
    if ls[i+1] > 1000000000:
        break
    i += 1
ls.pop(0)

n = int(input())
i = 0
c = 1

while True:
    if n <= int(ls[i]):
        print(c)
        break
    i += 1
    c += 1