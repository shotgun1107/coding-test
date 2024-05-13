n = int(input())
ls = list(map(int,input().split()))

M = ls[0]
c = 1
for i in range(1,n):
    if (M + ls[i]) % 2:
        M = ls[i]
        c += 1
print(c) 