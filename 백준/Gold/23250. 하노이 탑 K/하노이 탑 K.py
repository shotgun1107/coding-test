n,k = map(int,input().split())
def f(n, a,c,b):
    if n==0: return None

    if k1[0]-2**(n-1)+1<=0:
        f(n-1,a,b,c)
    else: 
        k1[0]=k1[0]-2**(n-1)+1
    k1[0] -= 1

    if k1[0]==0:
        print(a,c)
        exit(0)
    if k1[0]-2**(n-1)+1<=0:
        f(n-1,b,c,a)
    else:
        k1[0]=k1[0]-2**(n-1)+1
k1=[k]
f(n,1,3,2)