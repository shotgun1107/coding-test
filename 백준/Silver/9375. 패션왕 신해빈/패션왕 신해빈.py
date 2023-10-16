import math

for _ in range(int(input())):
    dic = {}
    ls = [tuple(input().split()) for _ in range(int(input()))]
    for i in ls:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 2
    print(math.prod(list(dic.values()))-1)