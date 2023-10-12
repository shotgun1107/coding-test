import math 

n, k = map(int,input().split())
ls = [ tuple(map(int,input().split())) for _ in range(n)]
man = [i[1] for i in sorted(list(filter(lambda x : x[0] == 1 , ls)),key= lambda x : x[1])]
woman = [i[1] for i in sorted(list(filter(lambda x : x[0] == 0 , ls)),key= lambda x : x[1])]

n = 0
for i in range(max(max(woman,default= -1),max(man,default= - 1))+1):
    n += math.ceil(man.count(i) / k)
    n += math.ceil(woman.count(i) / k)
print(n)