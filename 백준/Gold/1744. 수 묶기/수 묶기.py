answer = 0
zero_check = 0
negative_check = 0

positive_ls = []
negative_ls = []

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        answer +=1
    elif n == 0:
        zero_check = 1
    elif n < 0 :
        negative_check += 1
        negative_ls.append(n)
    else:
        positive_ls.append(n)
positive_ls = sorted(positive_ls)
negative_ls = sorted(negative_ls , reverse= True)

def even(ls):
    n = 0
    for i in range(int(len(ls) //2)):
        n += (ls[2*i] * ls[2*i+1])
    return n

def odd(ls):
    first = ls[0]
    n = 0
    for i in range(int(len(ls) //2)):
        n += (ls[2*i+1] * ls[2*(i+1)])
    return first , n

if positive_ls:
    if len(positive_ls) % 2:
        n , s = odd(positive_ls)
        answer = n + s + answer
    else:
        answer += even(positive_ls)

    if negative_check > 0:
        if negative_check % 2:
            negative_num , negative_sum_n = odd(negative_ls)
            if zero_check == 1:
                print(answer+negative_sum_n)
            else:
                print(answer+negative_num+negative_sum_n)
        else:
            print(answer + even(negative_ls))
    else:
        print(answer)
else:
    if negative_check > 0:
        if negative_check % 2:
            negative_num , negative_sum_n = odd(negative_ls)
            if zero_check == 1:
                print(answer+negative_sum_n)
            else:
                print(answer+negative_num+negative_sum_n)
        else:
            print(answer + even(negative_ls))
    else:
        print(answer)
