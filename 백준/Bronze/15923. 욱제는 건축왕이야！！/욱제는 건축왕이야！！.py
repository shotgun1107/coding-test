n = int(input())
min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')

for _ in range(n):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(2 * ((max_x - min_x) + (max_y - min_y)))