print((lambda a,b,c,d:min(a+d,b+c))(*map(int,open(0).read().split())))
