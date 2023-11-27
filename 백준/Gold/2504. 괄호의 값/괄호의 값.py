import sys

s = sys.stdin.readline().strip()

c = s
for _ in range(len(s)//2):
    c = c.replace('()','').replace('[]','')



if not c:
    dic = {'(' : 2 ,')' : 2, '[' : 3 , ']' : 3}
    stack = []
    answer = 0
    for i in range(len(s)):
        if s[i] in '([':
            stack.append(s[i])
        elif s[i-1] in '([':
            c = dic.get(s[i])
            stack.pop()
            for j in stack[::-1]:
                c *= dic.get(j)
            answer += c
        else:
            stack.pop()
    print(answer)

else:
    print(0)

