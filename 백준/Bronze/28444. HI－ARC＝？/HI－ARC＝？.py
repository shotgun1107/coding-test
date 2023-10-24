import math
ls = list(map(int,input().split()))
print(math.prod(ls[:2])-math.prod(ls[2:]))