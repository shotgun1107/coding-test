import math

a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
answer = []

for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                break
        else:
            answer.append(i)
print(*answer, -1, sep='\n')