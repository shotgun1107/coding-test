n = int(input())
ban = [list(map(int, input().split())) for _ in range(n)]
same = [[0] * n for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if ban[j][i] == ban[k][i]:
                same[k][j] = same[j][k] = 1

cnt = [s.count(1) for s in same]
print(cnt.index(max(cnt)) + 1)
