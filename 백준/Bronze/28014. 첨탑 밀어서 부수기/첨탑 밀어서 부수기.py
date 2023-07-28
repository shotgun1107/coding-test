n = int(input())
ls = [*map(int,input().split())]
cnt = 1
while ls:
    n = ls.pop()
    if  ls and not ls[-1] > n:
        cnt += 1
print(cnt)