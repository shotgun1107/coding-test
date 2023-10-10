def solution(arr, intervals):
    return sum([arr[x:y+1] for x, y in intervals], [])