def solution(arr, idx):
    return min([x for x,y in enumerate(arr) if x >= idx and y == 1],default= -1)