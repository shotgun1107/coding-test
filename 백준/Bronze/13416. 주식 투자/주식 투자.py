for _ in range(int(input())):
    t = 0
    for _ in range(int(input())):
        m = max(map(int, input().split()))
        if m >= 0:
            t += m
    print(t)
