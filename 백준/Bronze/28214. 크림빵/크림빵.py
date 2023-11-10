n,k,p = map(int,input().split())
ls = list(map(int,input().split()))
ls1 = [sum(ls[k*(i-1):k*i]) for i in range(1,n+1)]
print(sum([1 if i >= p else 0 for i in ls1]))