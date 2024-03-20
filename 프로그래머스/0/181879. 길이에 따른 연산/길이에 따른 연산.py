from math import prod as pd
solution = lambda ls : sum(ls) if len(ls) > 10 else pd(ls)