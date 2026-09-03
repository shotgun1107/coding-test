n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

m = 0

for i in range(n):
    for j in range(n-2):
        m = max(sum(ls[i][j:j+3]),m)
    
print(m)