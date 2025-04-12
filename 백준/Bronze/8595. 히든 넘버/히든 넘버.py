import re

print(sum(map(int, re.findall(r'\d+', open(0).read().split()[1]))))
