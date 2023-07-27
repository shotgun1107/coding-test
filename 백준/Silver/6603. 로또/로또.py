from itertools import *

while True:
    ls = []
    ls = list(map(int,input().split()))
    if ls[0] == 0:
        break
    k = ls.pop(0)
    ls1 = list(combinations(ls,6))
    for i in ls1:
        print(*i)
    print()