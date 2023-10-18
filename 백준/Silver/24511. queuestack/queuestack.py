import sys

input = sys.stdin.readline
input()

ls = []
answer = []

for x,y in zip( list(map(int,input().split())), list(map(int,input().split())) ):
    if x == 0:
        ls.append(y)

n = int(input())

ls = [*map(int,input().split())][::-1] + ls

print(*ls[-n:][::-1])