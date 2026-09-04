R, C = map(int, input().split())

first_row = input().split()
start = first_row[0]

col = [0] * C
ans = 0

for r in range(1, R - 1):
    row = input().split()
    prefix = 0

    for c in range(1, C - 1):
        old = col[c]

        if row[c] == start:
            ans += prefix

        prefix += old

        if row[c] != start:
            col[c] += 1

last_row = input().split()

if last_row[-1] == start:
    ans = 0

print(ans)