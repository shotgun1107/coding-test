from math import factorial 

c = 0
for i in str(factorial(int(input())))[::-1]:
    if i != '0':
        print(c)
        break
    c += 1