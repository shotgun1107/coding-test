def solution(arr, query):
    return [i for i in ls[0]] if (ls := [[arr := arr[:y+1]] if x % 2 else [arr := arr[y:]]  for x,y in enumerate(query,1)][-1]) else 0