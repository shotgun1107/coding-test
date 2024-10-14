n = int(input())
Y = 1000 - n
c = 0
while Y != 0:
    if Y - 500 >= 0: 
        Y -= 500
        c += 1
    elif Y - 100 >= 0: 
        Y -= 100
        c += 1
    elif Y - 50 >= 0: 
        Y -= 50
        c += 1
    elif Y - 10 >= 0: 
        Y -= 10
        c += 1
    elif Y - 5 >= 0: 
        Y -= 5
        c += 1
    else:
        Y -= 1
        c += 1
print(c)