from collections import deque
answer = []
for _ in range(int(input())):
    comand = input()
    non = input()
    ls = input()
    ls = eval(ls)
    ls = deque(ls)

    c = 0
    R = 0
    for cmd in comand:
        if cmd == 'R':
            R += 1
        else:
            if ls:
                if R % 2 == 0:
                    ls.popleft()
                else:
                    ls.pop()
            else:
                c = 1
                break
    if c == 0:
        if R % 2 == 0:
            ls = list(ls)
            print('[',end='')
            print(*ls,sep=',',end='')
            print(']')
        else:
            ls = list(reversed(ls))
            print('[',end='')
            print(*ls,sep=',',end='')
            print(']')
    else:
        print('error')

