def solution(num_list):
    return min([x for x,y in enumerate(num_list) if y < 0],default= -1)