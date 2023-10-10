def solution(my_string, indices):
    ls = [True for _ in range(len(my_string))]
    for i in indices:
        ls[i] = False
    return ''.join([y for x,y in enumerate(my_string) if ls[x]])