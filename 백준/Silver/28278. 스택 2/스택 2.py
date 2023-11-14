import sys
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    n = input().strip()
    
    if n == '2':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif n == '3':
        print(len(stack))
    elif n == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif n == '5':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    else:
        if ' ' in n:
            x, y = n.split()
            stack.append(y)
