import math


for _ in range(int(input())):
    r , n = map(int,input().split())
    print(math.comb(n, r))
     