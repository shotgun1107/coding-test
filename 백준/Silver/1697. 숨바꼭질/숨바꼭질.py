import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
chek = [0 for _ in range(100001)]	

bfs = deque([n])

while bfs:
    x = bfs.popleft()
    if x==k:	
        print(chek[x])
        break
    for i in [x-1, x+1, x*2]:	
        if 0<=i<=100000 and chek[i] == 0:
            chek[i] = chek[x]+1	
            bfs.append(i)