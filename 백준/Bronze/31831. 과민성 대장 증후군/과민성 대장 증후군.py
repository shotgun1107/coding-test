N,M = map(int,input().split())
s = 0
c = 0
for i in list(map(int,input().split())):
    s = s + i if s + i >= 0 else 0 
    if s >= M:
        c += 1
print(c)