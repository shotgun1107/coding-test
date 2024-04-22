from collections import deque

n = int(input())
ls = deque(list(map(int,input().split())))

c = 0
if n == 1 and ls[0] == 1:
    print(0)
else:
    for i in range(1,n+1):
        while ls:
            q = ls.popleft()
            if q == i:
                break
            else:
                c += 1
    print(c)