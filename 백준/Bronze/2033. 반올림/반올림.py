ls = list(map(int,input()))
for i in range(1,len(ls)):
    if ls[-1*i] >= 5:
        ls[(-1*i)-1] += 1
print(ls[0]*10**(len(ls)-1))