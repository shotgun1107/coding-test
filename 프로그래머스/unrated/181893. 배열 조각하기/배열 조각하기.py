def solution(arr, query):
    return [arr := arr[:y+1] if x % 2 else (arr := arr[y:])  for x,y in enumerate(query,1)][-1]