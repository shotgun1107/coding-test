n = int(input())
print(*['* '*n if not i % 2 else ' *'*n for i in range(n)],sep='\n')