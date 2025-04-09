n = int(input())
A = list(map(int, input().split()))

if n >= 3:
    d = A[1] - A[0]
    for i in range(2, n):
        if A[i] - A[i - 1] != d:
            print("NO")
            exit()
print("YES")
B = [0] * n 
print(" ".join(map(str, B)))
print(" ".join(map(str, A)))
