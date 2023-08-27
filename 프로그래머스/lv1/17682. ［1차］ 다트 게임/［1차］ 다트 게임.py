def solution(dartResult):
    dic = {'S': 1, 'D': 2, 'T': 3}
    intls = []
    answer = 0

    ls = [i for i in dartResult]
    len_ls = len(ls)

    i = 0
    while i < len_ls:
        if ls[i] == '1' and i + 1 < len_ls and ls[i+1] == '0':
            intls.append(10)
            i += 2
        elif '0' <= ls[i] <= '9':
            intls.append(int(ls[i]))
            i += 1
        elif ls[i] == '*':
            if len(intls) > 2:
                intls[1:] = list(map(lambda x: x * 2, intls[1:]))
            elif len(intls) > 1:
                intls = list(map(lambda x: x * 2, intls))
            else:
                intls[-1] *= 2
            i += 1
        elif ls[i] == '#':
            intls[-1] *= -1
            i += 1
        else:
            intls[-1] **= dic[ls[i]]
            i += 1
            
    return sum(intls)