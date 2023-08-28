from collections import deque

n, k = map(int, input().split())

people = deque(list(i for i in range(1, n+1)))
answer = []

while people:
    for _ in range(k-1):
        people.append(people.popleft())
    answer.append(people.popleft())

print("<",', '.join([str(x) for x in answer]),">",sep='')