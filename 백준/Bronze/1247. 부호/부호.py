import sys

for _ in range(3):
    ls = []
    for _ in range(int(sys.stdin.readline().strip())):
        ls.append(int(sys.stdin.readline().strip()))
    s = sum(ls)
    print('+' if s > 0 else '-' if s < 0 else '0')
