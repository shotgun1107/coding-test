import sys

input = sys.stdin.readline

N,K = map(int,input().split())
ls = [*map(int,input().split())]
n = sum(ls[:K])
m = n

for i in range(N-K):
    m = max(m,n := n - ls[i] + ls[i+K])

print(m)