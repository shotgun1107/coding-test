import sys
input = sys.stdin.readline

n = int(input())
ls = [int(input()) for _ in range(n)]

stack = []
answer = 0

for i in ls:
    cnt = 1
    if not stack:
        stack.append((i,cnt))
        continue
    for s in stack[::-1]:
        if s[0] > i:
            answer += 1
            break
        answer += s[1]
    while stack:
        s = stack.pop()
        if s[0] >= i:
            stack.append(s)
            break
    if stack and stack[-1][0] == i:
        cnt += stack.pop()[1]
        stack.append((i,cnt))
    else:
        stack.append((i,cnt))
print(answer)
# ls = "7 7 8 6 5 3 7 4 7 7 10 6 1 2".replace(' ','\n')
# print(ls)
