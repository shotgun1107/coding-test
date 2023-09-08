import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
a = 0
for i in range(n):
    a += (ord(s[i]) - 96) * 31**i
print(a)