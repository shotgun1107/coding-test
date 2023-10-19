dp = [1,3,5]

for _ in range(1001):
    dp.append(dp[-2]*2 + dp[-1])
print(dp[int(input())-1]%10007)