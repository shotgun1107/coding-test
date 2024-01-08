n = int(input())
ls = list(map(int,input().split()))

answer = 0

s = sum(ls)

for i in ls:
    answer += (s := s - i)*i
print(answer)