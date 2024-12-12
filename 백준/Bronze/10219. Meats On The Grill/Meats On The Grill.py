for _ in range(int(input())):
    n,_ = map(int,input().split())
    ls = [input() for _ in range(n)][::-1]
    print(*ls,sep='\n')