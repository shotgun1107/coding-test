ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))

ls1_c = 0
ls2_c = 0
c = False

for i in range(9):
    ls1_c += ls1[i]
    if ls1_c > ls2_c:
        c = True

    ls2_c += ls2[i]
    if ls1_c > ls2_c:
        c = True

print("Yes" if c else "No")
