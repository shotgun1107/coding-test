n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    dp[0][j][0] = matrix[0][j]
    dp[0][j][1] = matrix[0][j]
    dp[0][j][2] = matrix[0][j]

for i in range(1, n):
    for j in range(m):
        if j > 0:
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-1][1] + matrix[i][j])
            dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-1][2] + matrix[i][j])
        dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][0] + matrix[i][j])
        dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][2] + matrix[i][j])
        if j < m - 1:
            dp[i][j][2] = min(dp[i][j][2], dp[i-1][j+1][0] + matrix[i][j])
            dp[i][j][2] = min(dp[i][j][2], dp[i-1][j+1][1] + matrix[i][j])

min_fuel = float('inf')
for j in range(m):
    min_fuel = min(min_fuel, dp[n-1][j][0], dp[n-1][j][1], dp[n-1][j][2])

print(min_fuel)
