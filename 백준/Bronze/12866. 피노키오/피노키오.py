from collections import Counter
from math import prod

print(prod(Counter(input()).values()) % 1000000007 if int(input()) >= 4 else int(not(input())))