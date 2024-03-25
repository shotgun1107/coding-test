def solution(today, terms, privacies):
    answer = []
    today = (ls := list(map(int,today.split('.'))))[0] * 336 + ls[1] * 28 + ls[2]
    terms = {(ls:= list(i.split()))[0]:int(ls[1]) for i in terms}
    privacies = [ls[0] * 336 + ls[1] * 28 + ls[3] * 28 + ls[2] for ls in [[terms.get(k) if k.isalpha() else int(k) for j in i.split('.') for k in j.split()] for i in privacies]]
    
    return [idx for idx, i in enumerate(privacies, 1) if i <= today]


'''
1. 문자열 today를 int형을 바꾼다
2. terms를 공백기준으로 나누어 뒤에 있는 숫자를 int형으로 바꾼다
#privacies

'''
