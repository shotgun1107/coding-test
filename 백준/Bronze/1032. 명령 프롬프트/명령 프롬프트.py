n = int(input())
ls =[input() for _ in range(n)]
answer = [i for i in ls[0]]
ls.pop(0)
for i in ls:
    for j in range(len(i)):
        answer[j] = answer[j] if answer[j] == i[j] else '?'
print(''.join(answer))