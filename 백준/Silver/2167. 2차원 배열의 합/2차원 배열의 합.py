N,M = map(int,input().split())
ls = [ [*map(int,input().split())] for _ in range(N)]

for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    answer = 0
    for i in range(x2-x1+1):
        answer += sum(n := ls[x1+i-1][y1-1:y2])
    print(answer)