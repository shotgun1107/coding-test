ls = [[0]*100 for _ in range(100)]
n = int(input())

for _ in range(n):
    x,y = map(int,input().split())
    x -= 1
    y -=1
    for i in range(y,y+10):
        for j in range(x,x+10):
            ls[i][j] = 1

s = 0

for i in range(100):
    s += sum(ls[i])
print(s)