answer = []

while True:
    c = 0
    s = input()
    if s == '.':
        break
    s = ''.join([i for i in s if i =='(' or i == ')' or i == '[' or i == ']']) 

    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
            c = 1
        elif i == ')': 
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']': 
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        else:
            break
    if not stack:
        answer.append('yes')
    else:
        answer.append('no')

print(*answer,sep='\n')
