def solution(n, slicer, num_list):
    
    if n == 1:
        num_list = num_list[:slicer[1]+1]
    elif n == 2:
        num_list = num_list[slicer[0]:]
    elif n == 3:
        num_list = num_list[slicer[0]:slicer[1]+1]
    else:
        num_list = num_list[slicer[0]:slicer[1]+1:slicer[2]]
    return num_list