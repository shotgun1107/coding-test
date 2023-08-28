n = int(input())

def c():
    for N in range(1,n+1):
        s = str(N)
        ls = [int(i) for i in s]
        if N + sum(ls) == n:
            return N
    return 0

print(c())