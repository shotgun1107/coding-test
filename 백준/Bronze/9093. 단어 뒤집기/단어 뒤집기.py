for _ in range(int(input())):
    ls = list(input().split())
    for i in range(len(ls)):
        ls[i] = ls[i][::-1]
    print(*ls)