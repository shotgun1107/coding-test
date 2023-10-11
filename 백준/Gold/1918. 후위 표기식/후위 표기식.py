dic = {'+' : 1 , '-' : 1 , '*' : 10 , '/' : 10}
op = ['+','-','*','/' , '(']
stack = []

words = input().replace(' ' , '')
answer = []

for word in words:
    if word == ')':
        while True:
            if stack and stack[-1] != '(':
                answer.append(stack.pop())
            else:
                stack.pop()
                break
    elif word == '(':
        stack.append(word)
    elif not word in op:
        answer.append(word)
    else:
        while True:
            if stack and stack[-1]  != '(' and dic[stack[-1]] + 1 > dic[word]:
                answer.append(stack.pop())
            else:
                stack.append(word)
                break
print(*answer,*stack[::-1],sep='')