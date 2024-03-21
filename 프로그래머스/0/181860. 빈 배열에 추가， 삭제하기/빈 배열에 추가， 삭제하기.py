def solution(arr, flag):
    answer = []
    
    for i, v in enumerate(arr):
        for _ in range(v):
            if flag[i]:
                answer += [v, v]
            else:
                answer.pop()
    
    return answer
