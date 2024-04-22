ls = [i for i in range(1,int(input())+1)]

while not len(ls) == 1:
    ls = [i for idx , i in enumerate(ls) if idx % 2]
print(*ls)