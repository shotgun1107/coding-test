dic = {'.' : '.' , 'O' : 'O' , '-' : '|' , '|' : '-', '/' : '\\' , '\\' : '/' , '^' : '<' , '<' : 'v' , 'v' : '>' , '>' : '^'}

n,m = map(int,input().split())

ls = [input() for _ in range(n)]
ls1 = [[] for i in range(m)]

for i in range(m):
    for j in range(n):
        ls1[i].append(dic.get(ls[j][i]))
for i in ls1[::-1]:
    print(*i,sep='')