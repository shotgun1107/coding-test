while True:
    s = input()
    if s == '#':
        break
    c = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
            c += 1
    print(c)