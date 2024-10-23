from math import sqrt

bol = [False, False] + [True] * (1351)
primes = []

for i in range(2, 1351 + 1):
    if bol[i]:
        primes.append(i)
        for j in range(2 * i, 1351 + 1, i):
            bol[j] = False

def Lee_myunsoo(n):
    if n == '5':
        return False
    if int(n) < 4:
        return False
    if sum(int(i) for i in n) % 2 == 0:
        return False
    return True

def Lim_Hyunsoo(n):
    num = int(n)
    if num == 2 or num == 4:
        return True
    if num in primes or num == 1: 
        return False
        
    factors = set()
    temp = num
    for i in primes:
        if i * i > temp:
            break
        if temp % i == 0:
            factors.add(i)
            while temp % i == 0:
                temp //= i
    if temp > 1:
        factors.add(temp)
    return len(factors) % 2 == 0 

n = input()

if Lee_myunsoo(n) and Lim_Hyunsoo(n):
    print(4)
elif Lee_myunsoo(n):
    print(1)
elif Lim_Hyunsoo(n):
    print(2)
else:
    print(3)