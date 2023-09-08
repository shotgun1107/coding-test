n = int(input())
s = input()
a = 0
for i in range(n):
    a += (ord(s[i]) - 96) * 31**i
print(a)