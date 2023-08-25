ls = [2**i for i in range(1,16)]
ls1 = [3]

for i in range(len(ls)):
    ls1.append(ls1[i]+ls[i])
print(ls1[int(input())-1]**2)