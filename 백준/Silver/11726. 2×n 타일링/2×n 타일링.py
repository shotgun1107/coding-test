fibo = [0, 1]
p = 10001

for i in range(2,p):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo[int(input())+1] % 10007)