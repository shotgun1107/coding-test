from collections import Counter
for _ in range(int(input())):
    print(sorted(Counter([int(input()) for _ in range(int(input()))]).items() ,key= lambda x : (-x[1] , x[0]))[0][0])
