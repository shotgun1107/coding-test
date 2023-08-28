import math

n = int(input())
ls = [x*x for x in range(1, int(math.sqrt(n)) + 1)]
print(len(ls))
