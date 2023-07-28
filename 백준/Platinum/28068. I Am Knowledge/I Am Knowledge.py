import sys

ls = []
ls1 = []
ls2 = []
kimochi = 0
kimo = 1
for _ in range(int(sys.stdin.readline())):
    x,y = map(int,sys.stdin.readline().split())
    ls.append((x,y))
ls1 = list(filter(lambda x: x[0] <= x[1], ls))
ls1 = sorted(ls1,key = lambda x: (x[0], -x[1]))
ls2 = list(filter(lambda x: x[0] > x[1], ls))
ls2 = sorted(ls2,key = lambda x: (-x[1], x[0]))
ls = ls1 + ls2

for x in ls:
    if x[0] <= kimochi:
        kimochi -= x[0]
        kimochi += x[1]
    else:
        kimo = 0
        break
print(kimo)