ls = list(map(int,input().split()))

while ls != sorted(ls):
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]:
            ls[i] , ls[i+1] = ls[i+1] , ls[i]
            print(*ls)