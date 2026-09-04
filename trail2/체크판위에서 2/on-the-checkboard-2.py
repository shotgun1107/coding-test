R, C = map(int, input().split())

grid = [list(input().split()) for _ in range(R)]

start = grid[0][0]
end = grid[R - 1][C - 1]
ans = 0

if start != end:
    for c in range(1, C - 1):
        grid[0][c] = 0

    for r in range(1, R - 1):
        prefix = 0

        for c in range(1, C - 1):
            cur = grid[r][c]

            if cur == start:
                ans += prefix

            prefix += grid[0][c]

            if cur != start:
                grid[0][c] += 1

print(ans)