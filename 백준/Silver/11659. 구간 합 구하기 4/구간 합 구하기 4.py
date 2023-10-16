import sys
import itertools

input = sys.stdin.readline

n,m = map(int,input().split())
ls = [0] + list(itertools.accumulate([*map(int,input().split())]))
for _ in range(m):
    i,j = map(int,input().split())
    print(ls[j] - ls[i-1])