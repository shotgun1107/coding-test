solution = lambda arr ,n :  [num + n if idx % 2 == (len(arr) % 2 == 0) else num for idx, num in enumerate(arr)]

