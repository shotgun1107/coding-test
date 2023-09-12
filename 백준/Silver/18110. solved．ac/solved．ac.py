from collections import deque
import sys
input = sys.stdin.readline

ls = deque(sorted([int(input()) for _ in range(int(input()))]))

if len(ls) == 0:
    print(0)
else:
    for i in range(round(len(ls)*15/100+0.0000001)):
        ls.popleft()
        ls.pop()
    print(round(sum(ls)/len(ls)+0.0000001))