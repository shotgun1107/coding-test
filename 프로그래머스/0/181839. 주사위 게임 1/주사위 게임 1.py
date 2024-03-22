solution = lambda a, b: (a * a + b * b) if a % 2 == 1 and b % 2 == 1 else (2 * (a + b)) if a % 2 == 1 or b % 2 == 1 else abs(a - b)
