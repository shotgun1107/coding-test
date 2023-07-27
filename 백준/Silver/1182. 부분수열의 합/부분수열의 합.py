from itertools import *

n,m = map(int,input().split())

num = list(map(int,input().split()))

c = 0

for i in range(1,n+1):
    com = combinations(num,i)
    for j in com:
        j = list(j)
        if sum(j) == m:
            c += 1

print(c)