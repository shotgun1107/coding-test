from functools import cmp_to_key

def custom_compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return 1
    elif str(x) + str(y) < str(y) + str(x):
        return -1
    return 0

input()
ls = list(input().split())
if sum([int(i) for i in ls]) == 0:
    print(0)

else: 
    ls = sorted(ls, key=cmp_to_key(custom_compare), reverse=True)
    print(*[i for i in ls])