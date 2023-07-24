dic = {}

n = int(input())
ls = list(input().split())

for i in ls:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
        continue

n = int(input())
ls = list(input().split())

for i in ls:
    try:
        print(dic[i],end=' ')
    except:
        print(0,end = ' ')
        continue