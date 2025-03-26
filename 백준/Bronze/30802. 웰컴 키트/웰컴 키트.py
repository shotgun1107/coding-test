n = int(input())
ls = list(map(int, input().split()))
T, P = map(int, input().split())

t = sum((x + T - 1) // T for x in ls if x > 0)

p, pen = divmod(n, P)

print(t)
print(p , pen)