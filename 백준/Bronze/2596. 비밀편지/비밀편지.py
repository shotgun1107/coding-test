ls = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]
ls2 = "ABCDEFGH"
ls1 = []

n = int(input())
s = input()
s1 = ''
cnt = 0

for i in range(1, n + 1):
    ls1.append(s[(i - 1) * 6:i * 6])

for i in ls1:
    c = 0
    for j in range(8):
        n1 = 0
        for k in range(6):
            if i[k] != ls[j][k]:
                n1 += 1
        if n1 <= 1:
            s1 += ls2[j]
            c = 1
            break
    if c != 1:
        break
    cnt +=1
print(s1 if cnt == n else cnt+1)