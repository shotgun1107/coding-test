from collections import deque

n = int(input())
ls = list(map(int,input().split()))
dq = deque()
answer = [-1 for _ in range(n)]

for i in range(-1,-n-1,-1):
    while dq:
        s = dq.popleft()
        if s > ls[i]:
            dq.appendleft(s)
            answer[i] = s
            break
    dq.appendleft(ls[i])
print(*answer)