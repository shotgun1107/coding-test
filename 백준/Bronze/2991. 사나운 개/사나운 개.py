A,B,C,D = map(int,input().split())
ls = list(map(int,input().split()))

for n in ls:
    print(int((n-1) % (A+B) < A)+int((n-1) % (C+D) < C))
