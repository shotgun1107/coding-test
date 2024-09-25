n1, n2 = map(int, input().split())
a, b = input().split()

s = ''
for i in range(min(n1, n2)):
    s += a[i] + b[i]
s += a[min(n1, n2):] + b[min(n1, n2):]

dic = {'A': '3', 'B': '2', 'C': '1', 'D': '2', 'E': '4', 'F': '3', 'G': '1', 'H': '3', 'I': '1', 'J': '1', 'K': '3', 'L': '1', 'M': '3', 'N': '2', 'O': '1', 'P': '2', 'Q': '2', 'R': '2', 'S': '1', 'T': '2', 'U': '1', 'V': '1', 'W': '1', 'X': '2', 'Y': '2', 'Z': '1'}

num = ''.join(dic.get(d, '0') for d in s)

while len(num) > 2:
    new_num = ''
    for i in range(len(num) - 1):
        sum_digits = int(num[i]) + int(num[i+1])
        new_num += str(sum_digits % 10)
    num = new_num

num = num.lstrip('0') or '0'

print(f"{num}%")