def solution(arr):
    return arr[arr.index(2):-(arr[::-1].index(2)) if (arr[::-1].index(2)) != 0 else len(arr) ] if 2 in arr else [-1]