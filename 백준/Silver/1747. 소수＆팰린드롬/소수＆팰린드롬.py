import sys
ls = [2,2,3,5,5,7,7]
str1 = input()
if int(str1) < 8:
    print(ls[int(str1)-1])
else:
    while True:
        if len(str1) % 2 ==0:
            n = 1
        else:
            n = 0
        str2 = str1[:len(str1)//2-n:-1]
        str3 = str1[:len(str1)//2]
        if str2 == str3:
            d = 0
            for i in range(2,int(str1)):
                if int(str1) % i == 0:
                    d += 1
                    break
            if d != 0:
                    str1 = str(int(str1)+1)
            else:
                break
        else:
            str1 = str(int(str1)+1)
            continue
    print(str1)