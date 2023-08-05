from functools import cmp_to_key

def custom_compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return 1
    elif str(x) + str(y) < str(y) + str(x):
        return -1
    return 0

k , n = map(int,input().split())
ls = []
_max = 0

for _ in range(k):
    num = input()
    ls.append(num)
    _max = max(_max,int(num))

for _ in range(n-k):
    ls.append(str(_max))

ls = sorted(ls, key=cmp_to_key(custom_compare), reverse=True)


print(''.join(ls))