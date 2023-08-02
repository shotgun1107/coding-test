string = list(input())
answer = ''

answer += string.pop(0)
idx = 0
for i in range(len(string)):
    if answer[-1] >= string[i]:
        answer = answer + string[i]
    else:
        answer = string[i] + answer
print(answer[::-1])
