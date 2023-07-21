import math

ls = list(map(int,input().split()))

cnt = int(math.ceil((ls[2] - ls[0]) / (ls[0] - ls[1])))
print(cnt+1)