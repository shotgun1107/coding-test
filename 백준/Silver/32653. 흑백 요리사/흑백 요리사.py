from functools import reduce
from math import lcm
input()
print(reduce(lcm,list(map(int,input().split())))*2)