n = int(input())
ls = list(map(int,input().split()))

answer = 1

x = 1

for i in range(n-2,-1,-1):
    if x + 1 < ls[i]:
        x += 1
    else:
        x = ls[i]
    answer += x

print(answer)