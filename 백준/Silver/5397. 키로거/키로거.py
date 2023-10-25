for _ in range(int(input())):
    s = list(input())
    st1 = []
    st2 = []

    for word in s:
        if not word in '<>-':
            st1.append(word)
        elif word in '<>' :
            if word == '<' and st1:
                st2.append(st1.pop())
            elif word == '>' and  st2:
                st1.append(st2.pop())
        elif st1:
            st1.pop()
    print(''.join(st1+list(reversed(st2))))