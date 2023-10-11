from collections import Counter
import math

s = input()

c = Counter(s)

n = 0

if c.get('6'):
    n += c.get('6')
if c.get('9'):
    n += c.get('9')

print(max( max([y for x,y in c.items() if x != '6' and x != '9'],default= 0) ,math.ceil(n/2)))