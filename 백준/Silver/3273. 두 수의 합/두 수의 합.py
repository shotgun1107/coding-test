from collections import Counter

input()

ls = [*map(int,input().split())]
x = int(input())
c = dict(Counter(ls))
print(sum([c.get(x-i) for i in ls if c.get(x-i)])//2)