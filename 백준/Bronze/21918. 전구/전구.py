N,M = map(int,input().split())
ls = list(map(int,input().split()))
for _ in range(M):
    a,b,c = map(int,input().split())
    if a == 1:
        ls[b-1] = c
    else:
        for i in range(b-1,c):
            if a == 2:
                ls[i] = int(not(ls[i]))
            else:
                ls[i] = int(not(a == 3))
print(*ls)
