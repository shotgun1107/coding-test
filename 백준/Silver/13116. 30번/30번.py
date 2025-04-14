import os
[print(10*int(os.path.commonprefix([bin(a)[2:],bin(b)[2:]]),2)) for a,b in (map(int,input().split()) for _ in range(int(input())))]
