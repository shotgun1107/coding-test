solution = lambda ms, s: sum(1 for i in range(len(ms)) if ms.startswith(s, i))
