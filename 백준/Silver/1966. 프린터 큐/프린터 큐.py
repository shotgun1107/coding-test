from collections import deque

print_ls = []
for _ in range(int(input())):
    ls = []
    n,m = map(int,input().split())
    del_ls = [*map(int,input().split())]
    for x in range(n):
        y = del_ls[x]
        ls.append((x,y))
    ls = deque(ls)
    cnt = 0
    while True:
        max_value = max(ls, key=lambda x: x[1])[1]
        if ls[0][1] == max_value:
            p = ls.popleft()
            cnt += 1
            if p[0] == m:
                break
        else:
            ls.append(ls.popleft())

    print_ls.append(cnt)
    ls.clear()
    del_ls.clear()
print(*print_ls,sep='\n')