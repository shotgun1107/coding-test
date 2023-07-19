n = int(input())

n1,n2,n3 = map(int,input().split())
n4 = n2
n5 = 0 
n5 += n3

for _ in range(n-1):
    n1,n2,n3 = map(int,input().split())
    n4 = n4 / n1 * n2
    n5 += n3
print(0 if n5 % 2 == 0 else 1,end=' ')
print(int(n4))