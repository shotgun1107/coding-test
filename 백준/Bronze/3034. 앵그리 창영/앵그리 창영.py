from math import sqrt

N,W,H = map(int,input().split())
for _ in range(N):
    print('DA' if (n := int(input())) <= sqrt(W**2+H**2)else 'NE')