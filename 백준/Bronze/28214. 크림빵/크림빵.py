n,k,p = map(int,input().split())
ls = list(map(int,input().split()))
ls1 = [ls[k*(i-1):k*i] for i in range(1,n+1)]
print(sum([1 if i.count(0) < p else 0 for i in ls1]))