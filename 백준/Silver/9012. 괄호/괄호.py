for _ in range(int(input())):
    sum = 0
    re = 0
    parentheseslist = input()
    if len(parentheseslist)%2 != 0:
        print("NO")
    else:
        for i in range(len(parentheseslist)):
            if parentheseslist[i] == '(': sum += 1
            elif parentheseslist[i] == ')': sum -= 1
            if sum < 0:re += 1 ;break
        if re >= 1:print("NO")
        elif sum == 0:print("YES")
        else:print("NO")