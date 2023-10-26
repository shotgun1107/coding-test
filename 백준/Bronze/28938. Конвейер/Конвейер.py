input()
s = sum(list(map(int,input().split())))
print(['Left','Stay','Right'][(s >= 0) + (s > 0)])