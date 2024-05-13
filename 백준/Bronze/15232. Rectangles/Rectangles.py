n = int(input())
m = int(input())

print(*list('*'*m for _ in range(n)),sep='\n')