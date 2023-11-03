n = int(input())
ls = [int(input()) for _ in range(n)]

stack = []
result = []

for i in range(1,n+1):
    count = 0
    for _ in range(len(stack)):
        s = stack.pop()
        if s[0] < ls[-i]:
            count += s[1] + 1
        elif s[0] >= ls[-i]:
            stack.append(s)
            stack.append([ls[-i], count])
            break
    if len(stack) == 0:
        stack.append([ls[-i], count])
    
    result.append(count)

print(sum(result))