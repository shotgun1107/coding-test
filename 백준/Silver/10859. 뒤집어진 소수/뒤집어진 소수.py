import math

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n = input()

if set('347') & set(n) or not isprime(int(n)):
    print('no')
else:
    dic = {'6': '9', '9': '6'}
    num = int(''.join(dic.get(d, d) for d in n)[::-1])
    print('yes' if isprime(num) else 'no')