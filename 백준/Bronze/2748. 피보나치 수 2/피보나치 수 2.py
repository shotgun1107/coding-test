n = int(input())
ls = [0,1]
for _ in range(n-1):
    ls.append(sum(ls))
    del ls[0]
print(ls[1])