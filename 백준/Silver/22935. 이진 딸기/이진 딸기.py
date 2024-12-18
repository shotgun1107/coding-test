ls = [i for i in range(1,16)]+[i for i in range(14,1,-1)]

for _ in range(int(input())):   
    n = int(input())
    print(format(ls[((n-1)%28)], '04b').replace('0','V').replace('1','딸기'))
