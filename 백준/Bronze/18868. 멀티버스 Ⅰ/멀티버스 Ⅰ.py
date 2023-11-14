from itertools import combinations

n,m = map(int,input().split())

ncrn = list(combinations([i for i in range(n)],2))
ncrm = list(combinations([i for i in range(m)],2))

ls = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for i,j in ncrn:
    answer += int(all([1 if ls[i][x] < ls[i][y] and ls[j][x] < ls[j][y] else 1 if ls[i][x] == ls[i][y] and ls[j][x] == ls[j][y] else 1 if ls[i][x] > ls[i][y] and ls[j][x] > ls[j][y] else 0 for x, y in ncrm]))
print(answer)