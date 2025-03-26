answer = 0
c = 0

ls = []
for _ in range(int(input())):
    ls.append(tuple(map(int,input().split())))

ls = sorted(ls,key= lambda x : (x[1] , x[0]))

for i , j in ls:
    if c <= i:
        answer += 1
        c = j
print(answer)