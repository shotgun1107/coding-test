n = int(input())
ls = list(map(int,input().split()))
s = sum(ls)
answer = 0
for i in ls:
    s = s - i
    answer += s*i
print(answer)