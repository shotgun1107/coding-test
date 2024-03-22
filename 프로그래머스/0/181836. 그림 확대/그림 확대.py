def solution(picture, k):
    return ["".join(j * k for j in i) for i in picture for _ in range(k)]
