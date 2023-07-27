x, y, w, h = map(int, input().split())
ls = []
for i in range(4):
    ls.append(x)
    ls.append(y)
    ls.append(w - x)
    ls.append(h - y)
print(min(ls))