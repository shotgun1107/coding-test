import math


def isprime(n):
    for j in range(2, int(math.sqrt(n) + 1)):
            if n % j == 0:
                return False
    return True

for _ in range(int(input())):
    n = int(input())
    while True:
        if n == 0 or n == 1:
            print(2)
            break
        if isprime(n):
            print(n)
            break
        n +=1