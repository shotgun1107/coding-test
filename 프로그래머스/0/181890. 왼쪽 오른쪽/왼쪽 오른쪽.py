def solution(s : list):
    if 'l' in s and 'r' in s:
        if (l := s.index('l')) < (r :=  s.index('r')):
            return s[:l]
        else:
            return s[r+1:]
    elif 'l' in s :
        return s[:s.index('l')]
    elif 'r' in s:
        return s[s.index('r')+1:]
    return []