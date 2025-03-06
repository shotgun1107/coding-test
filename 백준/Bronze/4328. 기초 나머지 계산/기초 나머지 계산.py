while True:
    try:
        b,p,m = map(int,input().split())
        if (n := (int(f'{p}',b) % int(f'{m}',b))) == 0:
            print(n)
        else:
            result = ""
            while n > 0:
                remainder = n % b
                result = str(remainder) + result
                n //= b  
            print(result)
    except:
        break
