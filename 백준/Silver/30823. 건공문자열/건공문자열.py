import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = input().rstrip()
rotated = s[K-1:]
prefix = s[:K-1]
print(rotated + (prefix if (N-K) % 2 else prefix[::-1]))
