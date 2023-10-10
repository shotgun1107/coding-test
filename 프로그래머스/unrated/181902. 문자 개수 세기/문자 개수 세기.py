def solution(my_string):
    return [f'{my_string}'.count(chr(i).upper()) for i in range(97, 123)]+[f'{my_string}'.count(chr(i)) for i in range(97, 123)]