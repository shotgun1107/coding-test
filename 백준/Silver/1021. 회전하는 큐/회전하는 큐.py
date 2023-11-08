from collections import deque

n,m = map(int,input().split())
ls = deque(list(map(int,input().split())))
dq = deque([i for i in range(1,n+1)])
c = 0

for i in ls:
    if dq.index(i) > (len(dq)//2):
        while True:
            c += 1
            s = dq.pop()
            if s == i:
                break
            dq.appendleft(s)
    else:
        while True:
            s = dq.popleft()
            if s == i :
                break
            c += 1
            dq.append(s)
print(c)