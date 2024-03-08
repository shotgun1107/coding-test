from itertools import accumulate

N,M = map(int,input().split())
tv = [ [*map(int,input().split())] for _ in range(N)]
ls = [[0,*accumulate(tv[i]) ] for i in range(N)]

for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    answer = 0
    for i in range(x2-x1+1):
        answer += (ls[x1+i-1][y2] - ls[x1+i-1][y1-1])
    print(answer)
