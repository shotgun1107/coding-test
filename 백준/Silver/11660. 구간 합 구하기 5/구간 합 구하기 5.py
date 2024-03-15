import sys
import itertools

input = sys.stdin.readline

answer = []

N,M = map(int,input().split())
ls = [[0] + list(itertools.accumulate([*map(int,input().split())])) for _ in range(N)]

for _ in range(M):
    x1,y1,x2,y2 = map(int , input().split())
    s = 0
    for i in range(x1-1,x2):
        s += ls[i][y2] - ls[i][y1-1]
    answer.append(s)
print(*answer,sep='\n')
