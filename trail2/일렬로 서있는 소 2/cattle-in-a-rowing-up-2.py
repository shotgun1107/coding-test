from itertools import combinations

N = int(input())
A = list(map(int, input().split()))

print(len(list(filter(lambda x: x[0] <= x[1] <= x[2], combinations(A, 3)))))