n = int(input())
ls = []

for _ in range(n):
    x, y = map(int, input().split())
    ls.append((x, y))

answer = [0] * n

for i in range(n):
    x, y = ls[i]
    answer[i] = sum(1 for j in ls if x < j[0] and y < j[1])+1

print(*answer)
