from itertools import permutations

_ , M = map(int,input().split())

for i in permutations(sorted(list(map(int,input().split()))),M):
    print(*i)