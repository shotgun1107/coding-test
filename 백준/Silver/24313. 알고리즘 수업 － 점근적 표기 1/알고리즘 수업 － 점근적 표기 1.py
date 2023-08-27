a0,a1 = map(int,input().split())
c = int(input())
n = int(input())


print(1 if a0*n+a1 <= c*n and a0 <= c else 0)