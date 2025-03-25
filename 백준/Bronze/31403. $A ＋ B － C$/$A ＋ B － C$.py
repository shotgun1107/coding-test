print(sum(map(int,(ls:= open(0).read().split())))-(int(ls[-1])*2),int(''.join(ls[:2])) - int(ls[-1]),sep='\n')
