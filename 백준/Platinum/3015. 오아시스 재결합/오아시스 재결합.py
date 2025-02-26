import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0

for _ in range(n):
    h = int(input())
    cnt = 1
    
    while stack and stack[-1][0] <= h:
        answer += stack[-1][1]
        if stack[-1][0] == h:
            cnt += stack[-1][1]
        stack.pop()
    
    if stack:
        answer += 1
    
    stack.append((h, cnt))

print(answer)