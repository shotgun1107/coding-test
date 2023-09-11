for _ in range(int(input())):
    k = int(input())
    n = int(input())

    cmd = [[i for i in range(1,n+1)]] + [[] for i in range(k)]

    for i in range(1,k):
        for j in range(n):
            cmd[i].append(sum(cmd[i-1][:j+1]))
    print(sum(cmd[k-1][:n])) 