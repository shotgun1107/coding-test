import sys
from collections import deque

input = sys.stdin.readline
answer = []

word = input().rstrip()
ls = [[] for _ in range(26)]

ls[ord(word[0]) - 97].append(1)
for i in range(26):
    if not ls[i]:
        ls[i].append(0)

for i,s in enumerate(word[1:]):
    n = ord(s) - 97
    ls[n].append(ls[n][i]+1)
    for j in range(26):
        if not len(ls[j]) == i+2:
            ls[j].append(ls[j][i]+0)

for i in range(26):
    ls[i] = ls[i][::-1]
    ls[i].append(0)
    ls[i] = ls[i][::-1]

for _ in range(int(input())):
    n , x1 ,x2 = input().split()
    n , x1 , x2 = ord(n) - 97 , int(x1) , int(x2)
    answer.append(ls[n][x2+1] - ls[n][x1])
print(*answer,sep='\n')
