def solution(my_string, m, c):
    return ''.join([my_string[m*i:m*(i+1)][c-1] for i in range(len(my_string)//m)])
print(solution("ihrhbakrfpndopljhygc",4,2))