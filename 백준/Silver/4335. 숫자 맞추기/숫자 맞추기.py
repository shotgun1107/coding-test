ls = []

while (s := input()) != '0':
    ls.append(s)

c = ls.count('right on')

ls = [(int(ls[i]),ls[i+1]) for i in range(0,len(ls)-1,2)]
answer = list([x[0] for x in filter(lambda x : x[1] == 'right on',ls)])

for i in range(c):
    chek = True
    while ls:
        s = ls.pop(0)
        if s[1] == 'right on':
            ls.insert(0,s)
            break
        if s[1] == 'too high':
            if s[0] <= answer[i] :
                chek = False
                break
        else:
            if s[0] >= answer[i] :
                chek = False
                break
    while ls:
        if ls.pop(0)[1] == 'right on' :
            break
    if chek:
        print("Stan may be honest")
    else:
        print('Stan is dishonest')