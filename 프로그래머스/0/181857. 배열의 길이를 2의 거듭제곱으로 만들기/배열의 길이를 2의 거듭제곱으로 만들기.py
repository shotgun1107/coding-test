import math

solution = lambda arr: arr + [0] * (2**math.ceil(math.log2(len(arr))) - len(arr))