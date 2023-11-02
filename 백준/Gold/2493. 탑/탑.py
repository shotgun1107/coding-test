n = int(input())
ls = list(map(int,input().split()))
stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        s = stack.pop()
        if s[1] > ls[i]:
            stack.append(s)
            answer[i] = s[0]+1
            break
    stack.append((i,ls[i]))
print(*answer)