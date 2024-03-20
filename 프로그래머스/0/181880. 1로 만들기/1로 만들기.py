def solution(num_list):
    answer = 0
    for i in num_list:
        while True:
            if i == 1:
                break
            if i % 2:
                
                i = (i-1) // 2
            else:
                i //= 2
            answer += 1
    return answer
print(solution([12, 4, 15, 1, 14]))