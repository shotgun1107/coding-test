a,b,p,c,d,q = map(int,input().split())
print(int((d*p-b*q)/(a*d-b*c)),int((a*q-c*p)/(a*d-b*c)))