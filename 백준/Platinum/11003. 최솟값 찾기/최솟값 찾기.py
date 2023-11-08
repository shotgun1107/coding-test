import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int,input().split())
num = list(map(int, input().split()))
dq = deque()

for i in range(N):
    if dq and dq[0][0] <= i-L:
        dq.popleft()
    while dq and num[i] < dq[-1][1]:
        dq.pop()
    dq.append((i,num[i]))
    print(dq[0][1], end = " ")