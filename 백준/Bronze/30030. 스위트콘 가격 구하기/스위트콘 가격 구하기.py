ls = [i for i in range(100,11000,100)]
ls1 = [i + i // 10 for i in ls]
print(ls[ls1.index(int(input()))])