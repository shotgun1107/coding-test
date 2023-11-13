answer = []
chack = ([j+sum([int(k) for k in str(j)]) for j in range(1, 10001)])
for i in range(1,10001):
    if not i in chack:
        answer.append(i)
print(*answer,sep='\n')