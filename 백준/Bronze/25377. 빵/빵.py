ls = sorted(list(filter(lambda x : x[1] >= x[0] ,[ [*map(int,input().split())]  for _ in range(int(input()))])),key= lambda x : x[1] - x[0])
print(ls[0][1] if ls else -1)