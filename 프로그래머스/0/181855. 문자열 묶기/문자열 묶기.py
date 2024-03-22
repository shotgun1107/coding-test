from collections import Counter

solution = lambda ls : max(list(Counter(list(map(lambda x : len(x) ,ls))).values()))