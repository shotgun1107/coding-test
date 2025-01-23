input()
ls = list(map(int,input().split()))
c = 0
r = 0
for i in ls:
    if i == 1:
        c += 1
    else:
        c -= 1
    r += c
print(r)