N = int(input())

m = 1000000
fibo = [0, 1]
p = 100000*15

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= m

print(fibo[N%p])