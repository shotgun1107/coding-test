t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

maxTime = 3 * t1 + 20 * e1 + 120 * f1
melTime = 3 * t2 + 20 * e2 + 120 * f2

if maxTime > melTime:
    print("Max")
elif maxTime < melTime:
    print("Mel")
else:
    print("Draw")
