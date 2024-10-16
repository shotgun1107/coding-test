from math import ceil

X,Y = map(int,input().split())
Z = int(Y*100/X)
print(ceil((X*(Z+1)-(100*Y))/(100-Z-1)) if Z < 99 else -1)