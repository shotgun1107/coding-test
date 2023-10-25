for _ in range(int(input())):
    d, f, p = map(float, input().split())

    cost = d * f * p
    print(f"${cost:.2f}")