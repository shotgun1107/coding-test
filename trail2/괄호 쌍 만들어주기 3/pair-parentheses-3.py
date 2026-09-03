A = input()

answer = 0

for i, s in enumerate(A):
    if s != '(':
        continue
    answer += A[i:].count(')')
print(answer)