from collections import deque

ls = []
for _ in range(int(input())):
    ls.append(list(map(int, input().split())))

ls = deque(ls)

n = len(ls)
answer = [0 for i in range(n)]

for i in range(n):
    n1 = ls.popleft()
    x,y = n1
    for j in ls:
        x1 , y1 = j
        if x < x1 and y < y1:
            answer[i] += 1
    answer[i] += 1
    ls.append(n1)

print(*answer)