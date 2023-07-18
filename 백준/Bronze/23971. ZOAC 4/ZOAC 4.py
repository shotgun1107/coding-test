import math

n1, n2, n3, n4 = map(int, input().split())

row_count = math.ceil(n1 / (n3 + 1))
column_count = math.ceil(n2 / (n4 + 1))
c = row_count * column_count

print(c)
