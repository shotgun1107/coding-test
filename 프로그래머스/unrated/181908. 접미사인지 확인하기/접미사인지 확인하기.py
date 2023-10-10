def solution(my_string, is_suffix):
    return 1 if [i for i in sorted([my_string[i:] for i in range(len(my_string))]) if i == is_suffix] else 0