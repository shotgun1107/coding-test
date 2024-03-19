from itertools import accumulate
solution = lambda ls,n : [i for i in accumulate(ls) if i > n][0]