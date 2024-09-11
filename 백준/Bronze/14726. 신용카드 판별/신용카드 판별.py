for _ in range(int(input())):
    total = sum(
        int(n) if i % 2 else 
        (int(n) * 2 if int(n) * 2 < 10 else int(n) * 2 // 10 + int(n) * 2 % 10)
        for i, n in enumerate(input())
    )
    print('T' if total % 10 == 0 else 'F')