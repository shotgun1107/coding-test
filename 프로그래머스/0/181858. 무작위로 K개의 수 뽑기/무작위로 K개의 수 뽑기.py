def solution(arr, k):
    answer = []
    
    for i in arr:
        if len(answer) >= k:
            break
        if i not in answer:
            answer.append(i)
            
    if len(answer) < k: 
        answer.extend([-1] * (k - len(answer)))
    
    return answer