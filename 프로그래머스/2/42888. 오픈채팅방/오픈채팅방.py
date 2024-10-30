def solution(record):
    ls = []
    answer = []
    dic = {}
    for s in record:
        ls.append(s.split())
    for i in ls:
        if i[0] != "Leave":
            dic[i[1]] = i[2]
    for i in ls:
        if i[0] == 'Enter':
            answer.append(f'{dic[i[1]]}님이 들어왔습니다.')
        if i[0] == 'Leave':
            answer.append(f'{dic[i[1]]}님이 나갔습니다.')
    return answer