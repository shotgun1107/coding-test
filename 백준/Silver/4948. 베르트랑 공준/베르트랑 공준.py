# import math

# def isprime(n):
#     for i in range(2, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             return False
#     return True

# while True:
#     c = 0
#     n = int(input())
#     if n == 0:
#         break
#     for i in range(n+1,n*2+1):
#         if isprime(i):
#             c +=1
#     print(c)

n1= 246912
a = [False,False] + [True]*(n1-1)
primes=[]

for i in range(2,n1+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, n1+1, i):
        a[j] = False

while True:
    n = int(input())
    c = 0
    if n == 0:
        break
    for i in primes:
        if n < i:
            if i > 2*n:
                break
            c += 1
    print(c)