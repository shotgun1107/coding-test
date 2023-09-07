N,M = map(int,input().split())
ls = [ [*map(str,input())] for i in range(N)]

wb = ['WBWBWBWB','BWBWBWBW']

m = 100000

for q in range(N-8+1):
    M_check_ls= [[0 for i in range(M-8+1)],[0 for i in range(M-8+1)]]
    ls1 = ls[q:q+8]
    for i in range(M-8+1):
        for j in range(2):
            c = j
            for k in range(8):
                for x,y in zip(ls1[k][i:i+8],wb[c]):
                    if x != y:
                        M_check_ls[j][i] += 1
                c = int(not c)
    m = min(m,min(min(M_check_ls[0]),min(M_check_ls[1])))
    M_check_ls.clear()
print(m)