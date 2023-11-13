import math
import sys
input = sys.stdin.readline
prime = []
n = 1000000
check = [True] * (n+1)
for i in range(2, int(math.sqrt(n)) + 1):
    if check[i]:
        for j in range(i * 2, n + 1, i): 
            check[j] = False

for _ in range(int(input())):
    n =int(input())
    p = 0
    for i in range(2, n // 2 + 1):
        if check[i] and check[n - i]:
            p += 1
    print(p)
