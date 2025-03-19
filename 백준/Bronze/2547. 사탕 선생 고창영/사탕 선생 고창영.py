for _ in range(int(input())):
    q = input()
    N = int(input())
    ls = [int(input()) for i in range(N)]
    print("YES" if sum(ls)%N == 0 else "NO")