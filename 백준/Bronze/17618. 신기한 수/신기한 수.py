N = int(input())
count = 0

ds = 1
if 1 % ds == 0:
    count += 1

for i in range(2, N + 1):
    if (i - 1) % 10 != 9:
        ds += 1
    else:
        k = 0
        x = i - 1
        while x % 10 == 9:
            k += 1
            x //= 10
        ds = ds + 1 - 9 * k

    if i % ds == 0:
        count += 1

print(count)
