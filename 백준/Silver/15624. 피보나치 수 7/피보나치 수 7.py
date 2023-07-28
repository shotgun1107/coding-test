n = int(input())

if n <= 1:
    print(n)
else:
    a, b = 0, 1
    for i in range(n-1):
        c = a + b
        a = b% 1000000007
        b = c% 1000000007
    print(b)