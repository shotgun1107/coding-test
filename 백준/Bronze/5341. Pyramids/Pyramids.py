while True:
    if (n := int(input())) == 0:
        break
    print(sum([i for i in range(1,n+1)]))