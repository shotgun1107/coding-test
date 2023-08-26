n = int(input())
n1 = n
i  = 1


while True:
    n -= i
    if n <= 0:
        line = i
        break
    i += 1

line_first_num = 1
c = 0

for i in range(line):
    if i % 2 != 0:
        line_first_num += 1
        c += 4
    else:
        line_first_num += c


if line % 2 == 0:
    c = n1 - line_first_num
else:
    c = line_first_num - n1

num1 = 1
num2 = line
for i in range(c):
    num1 +=1
    num2 -= 1

print(f'{num1}/{num2}')
