n,s = input().split()
c = 0
stack = []

for i in s:
    if not i in stack:
        stack.append(i)
    else:
        c += 1
print('smupc_'+f'{1906+int(n)}{''.join(stack)}{c+4}'[::-1])