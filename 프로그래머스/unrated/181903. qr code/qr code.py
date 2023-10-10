def solution(q, r, code):
    return ''.join([word for index,word in enumerate(code) if index % q ==r])