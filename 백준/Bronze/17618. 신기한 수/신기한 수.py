c = 0
for i in range(1,int(input())+1):
    if not i % sum(map(int,str(i))):
        c += 1
print(c)